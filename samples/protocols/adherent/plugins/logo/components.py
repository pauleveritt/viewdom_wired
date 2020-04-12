from dataclasses import dataclass

from viewdom import html

from viewdom_wired import component
from samples.protocols.adherent.app.components import Logo
from samples.protocols.adherent.app.decorators import adherent


@component(for_=Logo)
@adherent(Logo)
@dataclass
class NoAltLogo:
    src: str

    def __call__(self):
        return html('<img src={self.src} />')
