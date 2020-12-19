from dataclasses import dataclass

from viewdom import html
from viewdom_wired import component


@component()
@dataclass
class Logo:
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
