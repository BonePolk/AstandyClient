import asyncio
import unittest
import threading
import os

from Astandy import StandClient
import tests_config

class BoltServiceTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_async_event(self):
        client = StandClient(tests_config.HANDSHAKE)
        signal = asyncio.Event()
        result = False  

        @client.MarketplaceRemoteEventListenerOnTradeRequestOpened()
        async def tradeOpened(client: StandClient, update):
            nonlocal result
            result = True
            signal.set()

        try:
            await asyncio.wait_for(client.start(), timeout=30)
            await client.subscribe_trade(44006)
            client.logger.info("Subscribed")
            await asyncio.wait_for(signal.wait(), timeout=30)
            
            self.assertTrue(result, "Maybe events don't working")
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  

    