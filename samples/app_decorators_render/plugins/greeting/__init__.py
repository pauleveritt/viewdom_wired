"""

A plugin that can be installed with pip and then register its components.

"""

from .greeting import Greeting
from ...app import App
from ...plugins import greeting


def setup(app: App):
    # Scan for decorators
    app.scanner.scan(greeting)
