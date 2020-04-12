from . import components  # noqa
from ...app import App
from .components import NoAltLogo


def setup(app: App):
    app.scanner.scan(components)


__all__ = [
    'NoAltLogo',
    'setup',
]
