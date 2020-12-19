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
    first_name = "Prop"
    result = render(html('<{Greeting} first_name={first_name} />'), container)

    expected = '<h1>Hello Prop</h1>'
    return expected, result
