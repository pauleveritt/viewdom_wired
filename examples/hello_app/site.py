"""
A simple site which uses (a) a pluggable app and (b) a plugin with some
known components.
"""

from viewdom import html

from viewdom_wired import render

# Get the pluggable app
from ..hello_app.app import make_app

# This site installed a plugin
from ..hello_app.plugin import Greeting


def main() -> str:
    registry = make_app(Greeting)
    container = registry.create_container()
    return render(html('<{Greeting}/>'), container)


expected = '<h1>Hello viewdom_wired</h1>'
