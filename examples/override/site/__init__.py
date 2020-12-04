"""
A package for a site that uses an installed app and some plugins.
"""

from . import components
from .views import greeting_view
from ..plugins import greeting
from ...app_decorators_render.app import App


def site_startup() -> App:
    # Make an app instance when the site starts up
    app = App()
    app.setup(greeting)

    # Make any site-specific registrations which might replace
    # one specific component or subcomponent from a plugin.
    app.scanner.scan(components)

    return app


def main() -> str:
    app = site_startup()
    vdom = greeting_view()
    return app.render(vdom)


expected = '<h1>Hello My Site</h1>'
