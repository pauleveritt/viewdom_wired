from dataclasses import dataclass

from viewdom import html, VDOM
from wired_injector import injectable

from ...app import Logo
from ...app.decorators import adherent


@injectable(for_=Logo)
@adherent(Logo)
@dataclass
class NoAltLogo:
    src: str

    def __call__(self) -> VDOM:
        return html('<img src={self.src} title="No alt Needed" />')
