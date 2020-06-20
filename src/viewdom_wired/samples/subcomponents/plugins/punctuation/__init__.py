"""
A plugin that can be installed with pip and then register its components.
"""

from . import punctuation
from .punctuation import Punctuation
from ...app import App


def setup(app: App):
    app.scanner.scan(punctuation)


__all__ = [
    'Punctuation',
    'setup'
]
