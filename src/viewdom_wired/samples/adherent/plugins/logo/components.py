from dataclasses import dataclass

from viewdom import html, VDOM

from viewdom_wired import component
from ...app import Logo
from ...app.decorators import adherent


@component(for_=Logo)
@adherent(Logo)
@dataclass
class NoAltLogo:
    src: str

    def __call__(self) -> VDOM:
        return html('<img src={self.src} title="No Alt Logo" />')
