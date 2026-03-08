from dataclasses import dataclass

class Extra:
    def __str__(self):
        return ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())

    def __repr__(self):
        return self.__str__
    
class ConnectionInfo(Extra):
    def __init__(self):
        self.ping: int = 0

        super().__init__()