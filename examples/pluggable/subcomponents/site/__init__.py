"""
A package for a site that uses an installed app and some plugins.
"""

from .views import greeting_view
from ..app import App
from ..plugins import greeting
from ..plugins import punctuation


def site_startup() -> App:
    # Make an app instance when the site starts up
    app = App()

    # Put a singleton for the punctuation character
    app.setup(greeting)
    app.setup(punctuation)
    return app


def main() -> str:
    app = site_startup()
    vdom = greeting_view()
    return app.render(vdom)


expected = '<h1>Hello viewdom_wired<span>!</span></h1>'
