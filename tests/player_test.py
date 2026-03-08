import asyncio
import unittest
import threading
import os

from Astandy import StandClient
import tests_config

class PlayerServiceTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_async_me(self):
        client = StandClient(
            tests_config.HANDSHAKE,
            host="82.211.7.47",
            port=51524,
            username="sport02iWN",
            password="23KFbNzprL"
        )
        result = False  

        try:
            await asyncio.wait_for(client.start(), timeout=30)
            result = await client.me()
            client.logger.info(f"{result}")
            
            self.assertTrue(result, "No profile! Why?")
        except asyncio.TimeoutError:
            self.fail("Connection timeout after 30 seconds")
        except Exception as ex:
            self.fail(f"Unexpected exception: {ex}")
        finally:
            await client.stop()  

    