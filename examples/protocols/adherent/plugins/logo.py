from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from ..app.decorators import adherent
from ..app.protocols import Logo


@component(for_=Logo)
@adherent(Logo)
@dataclass
class NoAltLogo:
    src: str
    alt: str = 'Alt'  # Comment this out to break the protocol

    def __call__(self) -> VDOM:
        return html('<img src={self.src} />')
