from .views import greeting_view
from ..app import App
from ..plugins import logo


def site_startup() -> App:
    app = App()
    # This site installed some plugins, load them
    app.setup(logo)
    return app


def main() -> str:
    app = site_startup()

    vdom = greeting_view()
    return app.render(vdom)
