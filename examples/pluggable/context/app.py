from viewdom import html
from wired_injector import InjectorRegistry

from viewdom_wired import render
from .plugins.greeting import Greeting
from .site import plugins
from .site.contexts import Customer


def main():
    # The app
    registry = InjectorRegistry()
    [registry.scan(plugin) for plugin in plugins]
    registry.scan()

    # Per "request"
    customer = Customer(name='Mary')
    container = registry.create_injectable_container(
        context=customer,
    )
    result = render(html('<{Greeting}/>'), container)

    expected = '<h1>Hello Mary</h1>'
    return expected, result
