from dataclasses import dataclass

from viewdom import html

from viewdom_wired import component
from .decorators import adherent
from .protocols import Logo, Navbar


@component(for_=Logo)
@adherent(Logo)
@dataclass
class DefaultLogo:
    src: str
    alt: str = 'Logo'

    def __call__(self):
        return html('<img src={self.src} />')


@component(for_=Navbar)
@adherent(Navbar)
@dataclass
class DefaultNavbar:
    logo_alt: str
    logo_src: str

    def __call__(self):
        return html('<nav><{Logo} alt={self.logo_alt} src={self.logo_src} /></nav>')
