"""
A simple example using (a) a pluggable app and (b) some known
components, both in their own files.
"""

from viewdom import html

from viewdom_wired import render
from ..app import App
from ..plugins import greeting
from ..plugins.greeting import Greeting  # noqa


def main() -> str:
    app = App()
    greeting.wired_setup(app.registry)
    container = app.registry.create_container()
    return render(html('<{Greeting}/>'), container)

expected = '<h1>Hello viewdom_wired</h1>'