class GMessage:
    def __init__(self, code: int, payload: bytes):
        self.code = code
        self.payload = payload