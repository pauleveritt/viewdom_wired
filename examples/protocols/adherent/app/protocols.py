from typing import Protocol

from viewdom_wired import Component


class Logo(Component, Protocol):
    alt: str


class Navbar(Component, Protocol):
    logo_alt: str
    logo_src: str
