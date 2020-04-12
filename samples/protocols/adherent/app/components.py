from dataclasses import dataclass
from typing import Protocol

from viewdom import html

from viewdom_wired import component
from .decorators import adherent


class Logo(Protocol):
    src: str
    alt: str

    def __call__(self) -> str: ...


@adherent(Logo)
@component()
@dataclass
class DefaultLogo:
    src: str
    alt: str = 'Logo'

    def __call__(self):
        return html('<img src={self.src} />')


@component()
@dataclass
class Navbar:
    logo_src: str

    def __call__(self):
        return html('<nav><{Logo} src={self.logo_src} /></nav>')
