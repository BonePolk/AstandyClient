from Astandy.generated.schemes_pb2 import GetPlayerRequest
from Astandy.types.service import Service
import Astandy

class PlayerRemoteService(Service):
    async def me(self: 'Astandy.StandClient'):
        '''
        Get handshake owner's player profile
        '''
        request = GetPlayerRequest()

        response = self.raw.PlayerRemoteService.getPlayer2Response(
            await self.send_request(
                *self.raw.PlayerRemoteService.getPlayer2Request(
                    request
                )
            )
        )

        return response

