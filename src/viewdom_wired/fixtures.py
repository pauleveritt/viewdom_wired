from typing import Protocol

from viewdom import VDOM


class Logo(Protocol):
    src: str
    alt: str

    def __call__(self) -> VDOM: ...
