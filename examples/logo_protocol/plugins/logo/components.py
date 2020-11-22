from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable

from ...app import Logo


@injectable(for_=Logo)
@dataclass
class NoAltLogo:
    src: str

    def __call__(self):
        return html('<img alt="No alt Needed" src={self.src} />')
