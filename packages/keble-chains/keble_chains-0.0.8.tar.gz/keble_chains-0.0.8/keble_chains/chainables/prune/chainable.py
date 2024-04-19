from ...typings.abc import ChainableABC
from typing import TypeVar, Generic

T = TypeVar('T')


class Prune(Generic[T], ChainableABC[T]):
    name: str = "prune"
    version: str = "default"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


