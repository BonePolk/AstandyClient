import asyncio
import unittest
import threading

from Astandy import StandClient
import tests_config

class CommunicationTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_async_ping(self):
        client = StandClient(tests_config.HANDSHAKE)
        result = False  

        try:
            await asyncio.wait_for(client.start(), timeout=30)
            result = await client.send_payload(b"\x01")
            self.assertTrue(result, "Client should be connected successfully or payload not sent")
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  

    async def test_async_request(self):
        client = StandClient(tests_config.HANDSHAKE)
        result = False  

        try:
            await asyncio.wait_for(client.start(), timeout=30)
            result = await client.send_request(1, b'\r\r\x086\x82^\x92\xc5\x92\x14I\xe2\xec\x0cp\x1dV\xe0\x1d\x11)O\x03\xe0V:\x9e{\xee,\x16\x8f\x014\xc9\x85\x8d\xcf\xac\xaa87\xc9\xca\x13]0\xe6\xdb\xb9#\xf5\xfa|A5\xa4\xe2\xd1\x1b&\x7f\xb4\xc3z\xdf\xa8\x08h>\xe7\xf3\x12\x89\xa5=\tY\x92\xdf\xe9\xb0\xbe\xda8c\x9bgnv\x1e\xe4N[\xfb/\xb2\xc0\xfdF]i\xb8\xbeG\xd1\x8a\x9c\x9fb]!\xca\xe8\x81|8\x01\xae/v\xc9\x0c\t\xa6<\xd4\x16\xc3\xd1\xb0YE\x14y\xc6\xd3L\xa4\xd6\x0e\xe1\xbeS\xce\xd4\xee\xa6\x82\xc0\x0bO\xda\xa3\x1f7\xe4f\xf8\xac')
            self.assertTrue(result, "Client should be connected successfully or not msg not sent or no response")
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  

    async def test_async_reconnect(self):
        client = StandClient(tests_config.HANDSHAKE, alias_name='Original')
        client2 = StandClient(tests_config.HANDSHAKE, alias_name='Second', reconnect_enable=False)
        result = False  

        try:
            await asyncio.wait_for(client.start(), timeout=30)

            try:
                await asyncio.wait_for(client2.start(), timeout=30)
                await client2.me()
                await asyncio.sleep(15)
            finally:
                await client2.stop()  

            result = await client.me()
            client.logger.info(f'{result}')
            
            self.assertTrue(result, "Client didn't reconnect successfully")
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  

    async def test_async_exception(self):
        client = StandClient("218225ecf75d2622114ec9dddbbc80b7", alias_name='Broken') 

        try:
            await asyncio.wait_for(client.start(), timeout=30)
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except ConnectionError:
            self.assertTrue(True, "Client didn't connected successfully")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  