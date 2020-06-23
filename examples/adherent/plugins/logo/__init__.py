from . import components
from .components import NoAltLogo
from ...app import App


def wired_setup(app: App):
    app.scanner.scan(components)


__all__ = [
    'NoAltLogo',
    'wired_setup',
]
