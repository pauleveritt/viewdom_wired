"""
A plugin that can be installed with pip and then register its components.
"""

from examples.context.app import App
from . import greeting
from .greeting import Greeting


def wired_setup(app: App):
    app.scanner.scan(greeting)


__all__ = [
    'Greeting',
    'wired_setup'
]