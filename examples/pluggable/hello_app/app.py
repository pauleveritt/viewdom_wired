from viewdom import html
from wired_injector import InjectorRegistry

from viewdom_wired import render
from .plugins.greeting import Greeting
from .site import plugins


def main():
    # The app
    registry = InjectorRegistry()
    [registry.scan(plugin) for plugin in plugins]
    registry.scan()

    # Per "request"
    container = registry.create_injectable_container()
    result = render(html('<{Greeting}><span>Children</span><//>'), container)

    expected = '<h1>Hello Site</h1>'
    return expected, result
