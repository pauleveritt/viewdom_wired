from . import components
from .components import NoAltLogo
from ...app import App


def setup(app: App):
    app.scanner.scan(components)


__all__ = [
    'NoAltLogo',
    'setup',
]
