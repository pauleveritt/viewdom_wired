"""
A plugin that can be installed with pip and then register its components.
"""

from . import greeting
from .greeting import Greeting
from ...app import App


def setup(app: App):
    app.scanner.scan(greeting)


__all__ = [
    'Greeting',
    'setup'
]
