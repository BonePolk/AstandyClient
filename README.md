# AstandyClient

An unofficial python client for the Standoff 2 game

## Installation

```
pip install astandy
```

## Usage example

You need to obtain handshake for your game account and push it as \_\_handshake\_\_

```
import asyncio

from Astandy import StandClient
from Astandy.generated.listeners import MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate

client = StandClient(__handshake__)

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

There also some docs on [readthedocs](https://astandyclient.readthedocs.io/en/latest/)

## About handshake

There some limitation with handshake:

- AxleBolt always try to fix ways to obtain handshake of account and also can add some new restrictions
- Only one active handshake per account (If you log into the official Standoff 2 game client, your current session will be invalidated, and you will need to perform a new handshake.)
- Handshake have limited lifetime 

## What do all this rpc methods actually?

Try it out and guess what difference

[!TIP]
Always use a test/alt account when exploring unknown methods to avoid any risks to your main profile.

Also i am planning to release application for analyzing the official Standoff 2 game client rpc behavior. News about are on [project telegram channel](https://t.me/astandy_api)
