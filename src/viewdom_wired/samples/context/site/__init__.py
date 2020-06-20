"""
A package for a site that uses an installed app and some plugins.
"""

from .contexts import Customer
from .views import greeting_view
from ..app import App
from ..plugins import greeting


def site_startup() -> App:
    # Make an app instance when the site starts up
    app = App()
    app.setup(greeting)

    return app


def main() -> str:
    app = site_startup()

    regular_customer = Customer(name='Mary')
    regular_vdom = greeting_view()
    return app.render(regular_vdom, context=regular_customer)
