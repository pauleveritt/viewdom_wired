from viewdom import html
from wired_injector import InjectorRegistry

from viewdom_wired import render
from .plugins.greeting import Greeting
from .site import plugins
from .site.contexts import FrenchCustomer


def main():
    # The app
    registry = InjectorRegistry()
    [registry.scan(plugin) for plugin in plugins]
    registry.scan()

    # Per "request"
    customer = FrenchCustomer(name='Marie')
    container = registry.create_injectable_container(
        context=customer,
    )
    result = render(html('<{Greeting}/>'), container)

    expected = '<h1>Bonjour Marie</h1>'
    return expected, result
