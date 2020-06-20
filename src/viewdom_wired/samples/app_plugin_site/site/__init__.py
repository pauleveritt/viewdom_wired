"""
A package for a site that uses an installed app and some plugins.
"""
from viewdom import html

from viewdom_wired import render
from ..app import make_app
from ..plugins import greeting
from ..plugins.greeting import Greeting  # noqa


def main() -> str:
    app = make_app()
    greeting.setup(app)
    container = app.create_container()
    return render(html('<{Greeting}/>'), container)
