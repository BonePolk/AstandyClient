# Examples

## Marketplace trade subscribe

An example showing how to subscribe to a skin trade on the marketplace and receive newly opened trade requests.

``` python
import asyncio

from Astandy import StandClient
from Astandy.generated.listeners import MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate

client = StandClient("e593bcefbd4ca98a53af13f3642ab9fe")

@client.MarketplaceRemoteEventListenerOnTradeRequestOpened()
async def trade_opened(client: StandClient, update: MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate):
    client.logger.info(f'Trade opened!')

async def main():
    await client.start()
    await client.subscribe_trade(44006)
    await client.idle()

if __name__ == "__main__":
    asyncio.run(main())
```

## Raw requests

An example showing how to use raw requests.
For an exmaple of raw request will be PlayerRemoteService.getPlayer2.

``` python
import asyncio

from Astandy import StandClient
from Astandy.generated.listeners import MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate

client = StandClient("e593bcefbd4ca98a53af13f3642ab9fe")

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