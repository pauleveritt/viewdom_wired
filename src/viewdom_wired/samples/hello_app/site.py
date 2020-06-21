"""
A simple site which uses (a) a pluggable app and (b) a plugin with some
known components.
"""

from viewdom import html

from viewdom_wired import render
# Get the pluggable app
from viewdom_wired.samples.hello_app.app import make_app
# This site installed a plugin
from viewdom_wired.samples.hello_app.plugin import Greeting


def main() -> str:
    registry = make_app(Greeting)
    container = registry.create_container()
    return render(html('<{Greeting}/>'), container)
