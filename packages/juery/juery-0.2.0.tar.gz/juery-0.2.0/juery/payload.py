from typing import Any, List, NamedTuple


class Payload(NamedTuple):
    path: List[str]
    key: str
    value: Any
