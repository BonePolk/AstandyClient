from Astandy.generated.schemes_pb2 import SubscribeRequest
from Astandy.types.service import Service
import Astandy

class BoltRemoteService(Service):
    async def subscribe(self: 'Astandy.StandClient', topic: str):
        '''
        :param topic: topic name
        '''
        request = SubscribeRequest()
        request.topic = topic

        response = self.raw.BoltRemoteService.subscribe2Response(
            await self.send_request(
                *self.raw.BoltRemoteService.subscribe2Request(
                    request
                )
            )
        )

        return True

    async def subscribe_trade(self: 'Astandy.StandClient', item_definition_id: int):
        return await self.subscribe(f"marketplace_trade_{item_definition_id}")
