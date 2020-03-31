"""

A simple example using (a) a pluggable app and (b) some known
components, both in their own files.


"""

from viewdom import html

from samples.hello_app.app import make_app
from samples.hello_app.components import Greeting
from viewdom_wired import render


def main() -> str:
    registry = make_app(Greeting)
    container = registry.create_container()
    return render(html('<{Greeting}/>'), container)
