"""

A package for a site that uses an installed app and some plugins.

"""

from .views import greeting_view
from ..app import App
from ..plugins import greeting
from . import components


def main() -> str:
    app = App()
    app.setup(greeting)

    # Make any site-specific registrations which might replace
    # one specific component or subocomponent from a plugin.
    app.scanner.scan(components)

    vdom = greeting_view()
    return app.render(vdom)
