from dataclasses import dataclass
from typing import Callable, Type, TypeVar

from typing_extensions import Protocol
from viewdom import html, VDOM

# from viewdom_wired import component
from viewdom_wired.fixtures import Logo

# from samples.protocols.adherent.app.decorators import adherent
protocol = TypeVar("protocol")


#
# @component(for_=Logo)
# @adherent(Logo)
# @dataclass
# class NoAltLogo:
#     src: str
#
#     def __call__(self):
#         return html('<img src={self.src} />')
#


# In wired, this decorator would also make a registration in the registry,
# as well as a constructor which sniffs the dataclass fields to do the DI.
def component(c: Callable[[], protocol]) -> Callable[[Type[protocol]], Type[protocol]]:
    def decor(input_value: Type[protocol]) -> Type[protocol]:
        return input_value

    return decor

#
# class Logo(Protocol):
#     src: str
#     alt: str
#
#     def __call__(self) -> VDOM: ...


@component(Logo)
@dataclass
class NoAltLogo:
    # src: str
    # alt: str

    def __call__(self) -> VDOM:
        return html('<img src={self.src} />')
