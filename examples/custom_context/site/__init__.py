"""
A package for a site that uses an installed app and some plugins.
"""
from typing import Dict

from . import components
from .contexts import Customer, FrenchCustomer
from .views import greeting_view
from ..plugins import greeting
from ...context.app import App


def site_startup() -> App:
    # Make an app instance when the site starts up
    app = App()
    app.setup(greeting)

    # Replace plugin.greeting.Greeting with a different
    # implementation for this site
    app.scanner.scan(components)

    return app


def main() -> Dict[str, str]:
    app = site_startup()

    # Regular customer
    regular_customer = Customer(name='Mary')
    regular_vdom = greeting_view()
    regular_result = app.render(regular_vdom, context=regular_customer)

    # French customer
    french_customer = FrenchCustomer(name='Marie')
    french_vdom = greeting_view()
    french_result = app.render(french_vdom, context=french_customer)

    return dict(regular_result=regular_result, french_result=french_result)


expected = dict(
    regular_result='<h1>Hello Mary</h1>',
    french_result='<h1>Bonjour Marie</h1>',
)
