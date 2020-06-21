from dataclasses import dataclass

from viewdom import html

from viewdom_wired import component
from ...app import Logo


@component(for_=Logo)
@dataclass
class NoAltLogo:
    src: str

    def __call__(self):
        return html('<img src={self.src} />')
