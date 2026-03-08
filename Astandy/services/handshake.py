from secrets import token_bytes

from Astandy.generated.schemes_pb2 import GACHFBFBBEHDAAD
from Astandy.types.service import Service
import Astandy

class HandshakeRemoteService(Service):
    async def handshake(self: 'Astandy.StandClient', handshake: str):
        request = GACHFBFBBEHDAAD()
        request.GFCCADHDDFAFHFE = handshake

        
        response = self.raw.HandshakeRemoteService.encryptedHandshakeResponse(
            await self.send_request(
                *self.raw.HandshakeRemoteService.encryptedHandshakeRequest(
                    request,
                    self.cipher
                )
            ),
            self.cipher
        )

        return True
