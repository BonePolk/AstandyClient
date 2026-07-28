from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class RpcTarget:
    code: int
    service: str
    method: str
    request: bytes | Sequence[bytes] | None = None
    
    @property
    def use_method_names(self) -> bool:
        return self.code == 0
