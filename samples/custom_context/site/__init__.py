"""

A package for a site that uses an installed app and some plugins.

"""
from typing import Dict

from .contexts import Customer, FrenchCustomer
from .views import greeting_view
from ..app import App
from ..plugins import greeting
from . import components


def main() -> Dict[str, str]:
    app = App()

    # First setup each plugin
    app.setup(greeting)

    # Last, replace plugin.greeting.Greeting with a
    # different implementation for this site
    app.scanner.scan(components)

    # Regular customer
    regular_customer = Customer(name='Mary')
    regular_vdom = greeting_view()
    regular_result = app.render(regular_vdom, context=regular_customer)

    # French customer
    french_customer = FrenchCustomer(name='Marie')
    french_vdom = greeting_view()
    french_result = app.render(french_vdom, context=french_customer)

    return dict(
        regular_result=regular_result,
        french_result=french_result
    )
