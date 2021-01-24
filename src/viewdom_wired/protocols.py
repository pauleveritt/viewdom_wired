from viewdom import VDOM

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol  # type: ignore # noqa: F401


class Component(Protocol):
    def __call__(self) -> VDOM:
        ...
