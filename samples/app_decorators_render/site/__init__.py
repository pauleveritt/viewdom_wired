"""

A package for a site that uses an installed app and some plugins.

"""

from .views import greeting_view
from ..app import App
from ..plugins import greeting


def main() -> str:
    app = App()
    app.setup(greeting)
    vdom = greeting_view()
    return app.render(vdom)
