from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable

from .decorators import adherent
from .protocols import Logo, Navbar


@injectable(for_=Logo)
@adherent(Logo)
@dataclass
class DefaultLogo:
    src: str
    alt: str = 'Logo'

    def __call__(self):
        return html('<img src={self.src} />')


@injectable(for_=Navbar)
@adherent(Navbar)
@dataclass
class DefaultNavbar:
    logo_alt: str
    logo_src: str

    def __call__(self):
        return html('<nav><{Logo} alt={self.logo_alt} src={self.logo_src} /></nav>')
