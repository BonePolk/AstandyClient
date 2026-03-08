import asyncio
import unittest
import threading
import os

from Astandy import StandClient
import tests_config

class BaseTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_async_base(self):
        client = StandClient(tests_config.HANDSHAKE)
        try:
            await client.start()

            self.assertTrue(True)
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()

    async def test_async_on_connect(self):
        client = StandClient(tests_config.HANDSHAKE)
        connected = asyncio.Event()

        @client.OnConnect()
        async def connect(client: StandClient, update):
            connected.set()

        try:
            await client.start()
            await asyncio.wait_for(connected.wait(), timeout=30)
            self.assertTrue(True)
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            client.logger.info('Stopping!')
            await client.stop()

