# AstandyClient

An unofficial python client for the Standoff 2 game

## Installation

```
pip install astandy
```

## Usage example

You need to get handshake for your game account and push it as \_\_handshake\_\_

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
