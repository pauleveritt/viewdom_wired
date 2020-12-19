from viewdom import html
from wired_injector import InjectorRegistry

from viewdom_wired import render
from .components import Greeting


def main():
    # The app
    registry = InjectorRegistry()
    registry.scan()

    # Per "request"
    container = registry.create_injectable_container()
    result = render(html('<{Greeting}/>'), container)

    expected = '<h1>Hello viewdom_wired</h1>'
    return expected, result
