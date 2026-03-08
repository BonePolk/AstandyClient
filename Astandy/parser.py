from Astandy.schemes.messages_pb2 import ClientMsg, BinaryValue, ServerMsg


class Parser:
    @staticmethod
    def new_msg(uuid: str, code: int, payload: bytes):
        msg = ClientMsg()
        msg.id = uuid
        msg.code = code
        msg.data.append(BinaryValue())
        msg.data[0].one = payload

        return msg.SerializeToString()
    
    @staticmethod
    def parse_response(request: bytes) -> ServerMsg:
        msg = ServerMsg()
        msg.ParseFromString(request)

        return msg
