"""

A package for a site that uses an installed app and some plugins.

"""
from typing import Dict

from .contexts import Customer
from .views import greeting_view
from ..app import App
from ..plugins import greeting


def main() -> str:
    app = App()
    app.setup(greeting)

    regular_customer = Customer(name='Mary')
    regular_vdom = greeting_view()
    return app.render(regular_vdom, context=regular_customer)
