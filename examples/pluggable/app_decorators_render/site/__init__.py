"""
A package for a site that uses an installed app and some plugins.
"""

from .views import greeting_view
from ..app import App
from ..plugins import greeting


def site_startup() -> App:
    # Make an app instance when the site starts up
    app = App()
    app.setup(greeting)
    return app


def main() -> str:
    """ Make an app and process a request """

    app = site_startup()
    vdom = greeting_view()
    return app.render(vdom)


expected = '<h1>Hello viewdom_wired</h1>'
