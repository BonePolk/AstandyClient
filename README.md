# AstandyClient

An *unofficial python client* for the Standoff 2 game

📢 **News: [Project Telegram Channel](https://t.me/astandy_api)**

📚 **Documentation: [readthedocs](https://astandyclient.readthedocs.io/en/latest/)**

## Installation

```bash
pip install astandy
```

## Usage example

You need to obtain handshake for your game account and pass it to client

```python
import asyncio

from Astandy import StandClient
from Astandy.generated.services import GetPlayerRequest
from Astandy.generated.listeners import MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate

client = StandClient("__your_handshake_here__")

async def main():
    await client.start()

    request = GetPlayerRequest()

    response = client.raw.PlayerRemoteService.getPlayer2Response(
        await client.send_request(
            *client.raw.PlayerRemoteService.getPlayer2Request(
                request
            )
        )
    )

    client.logger.info(f'getPlayer2 response: {response}')

    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## About handshake

There some limitation with handshake:

- AxleBolt always try to fix ways to obtain handshake of account and also can add some new restrictions
- Only one active handshake per account (If you log into the official Standoff 2 game client, your current session will be invalidated, and you will need to perform a new handshake.)
- Handshake have limited lifetime must be refreshed periodically

## What do all this rpc methods actually?

- Try it out
- And observe differences on account maybe or simply guess idk

**Always use a test account when exploring unknown methods to avoid any risks to your main profile.**

Also i am planning to release application for analyzing the official Standoff 2 game client rpc behavior. 

## Supported RPC methods

There not all supported rpc methods implemented. I am already fix tools to autogen all rpc methods from game dump and i am planning to add them later.
