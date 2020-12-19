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
        return html('<img src={self.src} alt="Logo" />')


@component(for_=Navbar)
@dataclass
class DefaultNavbar:
    logo_src: str

    def __call__(self):
        return html('<nav><{Logo} src={self.logo_src} /></nav>')
