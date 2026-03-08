import asyncio
import socket
import ssl
from threading import Thread, Event
from time import sleep
from uuid import uuid4

import lz4.block
from python_socks.async_.asyncio import Proxy
from python_socks._types import ProxyType

from .dispatcher import Dispatcher
from .cipher import AstandyCipher
from .events import BaseEvents
from .types.extras import ConnectionInfo
from .generated import Generated, CADATA, GeneratedEvent, GENERATED_UPDATES, UPDATE_INDEX
from .services import Services
from .logging import AstandyLoggers
from .updates import Connected
from .utils import run_on_uvloop
from .parser import Parser
from .schemes.messages_pb2 import Response, ServerMsg
from .errors import AstandyRPCException

REQUEST_TIMEOUT = 15


class StandClient(Services, BaseEvents, Generated):
    """
    Client, the main means for interacting with game server.

    :param handshake: Handshake to authorize client
    :param ping_timeout: [Default: 15] Maximum time (in seconds) to wait for a ping response.
    :param alias_name: [Default: class name] The name of the client used in custom logging.
    :param reconnect_enable: [Default: True] If it is True client will try to reconnect after connection closed
    """
    SERVER_HOST = "server.boltgaming.io"
    SERVER_PORT = 2223

    def __init__(self, 
                 handshake: str, 
                 ping_timeout=15, 
                 alias_name = '', 
                 reconnect_enable=True,
                 host=None,
                 port=None,
                 username=None,
                 password=None,
                 max_retry_count=3
            ):
        super().__init__()
        Services.__init__(self)
        
        self.ping_timeout = ping_timeout
        self.reconnect_enable = reconnect_enable
        self.proxy_host = host
        self.proxy_port = port
        self.proxy_username = username
        self.proxy_password = password
        self.max_retry_count = max_retry_count

        self._handshake = handshake
        if not alias_name: alias_name = self.__class__.__name__
        
        self._dp = Dispatcher(self)
        self._reader: asyncio.StreamReader = None
        self._writer: asyncio.StreamWriter = None
        self._sock: socket.socket = None
        self._loop = None

        self._running = False
        self._stopped = False
        self._is_first_connect = True
        self._connect_attempts_number = 0
        self._connect_info: ConnectionInfo = ConnectionInfo()
        self._pending_ping: asyncio.Event = asyncio.Event()
        self._reconnecting: asyncio.Event = asyncio.Event()
        self._pending_requests: dict[str, asyncio.Future] = {}

        self._connected = asyncio.Event()
        self._disconnected = asyncio.Event()
        self._send_lock = asyncio.Lock()
        self._authenticated = asyncio.Event()

        self.cipher: AstandyCipher
        self._logger = AstandyLoggers.get_logger(alias_name)

    @property
    def logger(self):
        return self._logger
    
    async def _connect_proxy(self):
        proxy = Proxy(
            proxy_type=ProxyType.SOCKS5,
            host=self.proxy_host,
            port=self.proxy_port,
            username=self.proxy_username,
            password=self.proxy_password
        )

        return await proxy.connect(
            dest_host=StandClient.SERVER_HOST,
            dest_port=StandClient.SERVER_PORT
        )

    async def _connect(self):
        await self._disconnect()

        context = ssl.create_default_context()
        if not CADATA:
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
        else:
            context.load_verify_locations(cadata=CADATA)

        host = StandClient.SERVER_HOST
        port = StandClient.SERVER_PORT
        sock = None
        if self.proxy_host and self.proxy_port:
            host = None
            port = None
            self._sock = await self._connect_proxy()

        self._reader, self._writer = await asyncio.open_connection(
            host=host, 
            port=port, 
            sock=self._sock,
            ssl=context,
            server_hostname=StandClient.SERVER_HOST
        )

        self._running = True 

    async def _disconnect(self):
        try:
            if self._writer:
                self._writer.close()
                await self._writer.wait_closed()
            
            if self._sock:
                self._sock.close()
        except ssl.SSLError:
            self.logger.warning('Server sent data after connection closed!')

        self._disconnected.set()
        self._authenticated.clear()
        self._connected.clear()

    async def start(self):
        """
        Start the client.

        This method connects the client to game.
        :raises ConnectionError: If the connection to game servers fails
        """    
        self._run_task = asyncio.create_task(self._run())
        wait_task = asyncio.create_task(self._authenticated.wait())

        done, pending = await asyncio.wait(
            [self._run_task, wait_task],
            return_when=asyncio.FIRST_COMPLETED
        )

        if self._run_task in done:
            self._authenticated.set()
            await wait_task
            if self._run_task.exception(): raise self._run_task.exception()

    async def idle(self):
        """
        Block thread while client running.

        """
        while self._running:
            await asyncio.sleep(0.1)
        
        
    async def _run(self):
        self._loop = asyncio.get_event_loop()

        while not self._stopped and (self.reconnect_enable or self._is_first_connect):
            self._connect_attempts_number += 1

            if self._connect_attempts_number > self.max_retry_count: raise ConnectionError

            if not self._is_first_connect: self.logger.info('Reconnecting!')
            self.cipher = AstandyCipher()
            self.generate_keys()
            
            try:
                await self._connect()
                self._connected.set()

                asyncio.create_task(self._initialize())
            except Exception as e:
                self.logger.warning(f'Connection failed {e}!')


            await self._read_loop()

            await self._disconnect()

    async def _initialize(self):
        try:
            await self.hello()
            await self.handshake(self._handshake)
            asyncio.create_task(self._ping_loop())
            self._authenticated.set()

            if not self._is_first_connect: self.logger.info('Reconnected!')
            self._is_first_connect = False
            self._connect_attempts_number = 0

            await self._dp.call_listeners(Connected())
        except AstandyRPCException as ex:
            self.logger.critical(f'Failed to authorize {ex}!')
            self._running = False
        

    async def _read_loop(self):
        while self._running:
            await asyncio.sleep(0.001)
            msg_leng = await self._read_header()
            if msg_leng <= 0: continue
            
            msg = await self._read_exactly(msg_leng, timeout=1)
            if not msg: continue

            if msg == b'\x01': 
                self._pending_ping.set()
                continue
            
            asyncio.create_task(self._handle_msg(Parser.parse_response(msg)))
        self._running = False

    async def _ping_loop(self):
        self._logger.extra = self._connect_info
        while self._running:
            self._pending_ping.clear()
            start_time = asyncio.get_event_loop().time()

            if not await self.send_payload(b'\x01'):
                self._logger.critical('Failed to send ping!')
            try:
                await asyncio.wait_for(self._pending_ping.wait(), timeout=self.ping_timeout)
            except asyncio.TimeoutError:
                self._running = False
                self._logger.critical('Ping not received!')
                break
            
            self._connect_info.ping = int((asyncio.get_event_loop().time() - start_time) * 1000)
            
            await asyncio.sleep(5)
        

    async def _read_exactly(self, size: int, timeout: float = 0.1) -> bytes | None:
        try:
            return await asyncio.wait_for(self._reader.readexactly(size), timeout=timeout)
        except asyncio.TimeoutError:
            return None
        except asyncio.IncompleteReadError:
            self._running = False
            self._logger.critical("Connection closed by server!")
            return None
        except Exception as e:
            self._logger.exception(f"Unexpected error while sending payload: {e}")
            return None

    async def _read_header(self):
        header = await self._read_exactly(4)
        if not header: return -1
        return int.from_bytes(header, byteorder='big')
    
    async def _handle_msg(self, server_msg: ServerMsg):
        for response in server_msg.responses:
            if response.id in self._pending_requests:
                self._pending_requests[response.id].set_result(response)
            else:
                self._logger.warning(f"Skipped {response.id} response!")
        
        for event in server_msg.events:
            if GeneratedEvent.has_value(event.code):
                await self._dp.call_listeners(GENERATED_UPDATES[event.code][UPDATE_INDEX[event.code]](event.params.one))
            else:
                self.logger.warning(f"Unknown event code {event.code}!")

        for compressed in server_msg.compressed_instances:
            data = lz4.block.decompress(compressed.compressed, uncompressed_size=compressed.uncompressed_size)
            await self._handle_msg(Parser.parse_response(data))
    
    async def send_request(self, code:int, request: bytes) -> Response:
        """
        Sending request to game servers

        :param code: RPC method code
        :param request: RPC payload
        """
        uuid = str(uuid4())
        future = asyncio.get_event_loop().create_future()
        self._pending_requests[uuid] = future

        result: Response = Response()
        if not await self._send_payload(Parser.new_msg(uuid, code, request)):
            self._pending_requests.pop(uuid)
            raise ConnectionError("Failed to send payload: Connection lost or closed.")
        
        try:
            result = await asyncio.wait_for(future, timeout=REQUEST_TIMEOUT)
        except asyncio.TimeoutError:
            self._logger.warning(f"Request {uuid} timeout after {REQUEST_TIMEOUT} seconds")
        finally:
            self._pending_requests.pop(uuid)

        return result

    async def _send_payload(self, payload):
        await self._connected.wait()
        if not self._running or not self._writer: return False

        async with self._send_lock:
            try:
                self._writer.write(len(payload).to_bytes(4, byteorder='big')+payload)
                await self._writer.drain()
                return True
            except (BrokenPipeError, ConnectionResetError):
                self._logger.critical("Connection lost while sending data.")
                return False
            except Exception as e:
                self._logger.exception(f"Unexpected error while sending payload: {e}")
                return False
    
    async def send_payload(self, payload: bytes):
        """
        Sends a payload to the server.

        :param payload: The data to be sent.
        :return: True if the payload was successfully sent else False.
        """
        if not await self._send_payload(payload):
            self._running = False
            return False
        return True

    async def stop(self):
        """
        Stop the client.
        """
        if not self._running: return
        self._disconnected.clear()
        self._stopped = True
        self._running = False
        await self._disconnected.wait()

    
    