from viewdom import html
from viewdom_wired import render
from wired_injector import InjectorRegistry

from .components import Navbar
from .. import site


def main():
    # The app
    registry = InjectorRegistry()
    # Scan the app, then the plugins, then the site
    registry.scan()
    [registry.scan(plugin) for plugin in site.plugins]
    registry.scan(site)

    # Per "request"
    container = registry.create_injectable_container()
    LOGO_SRC = 'logo.png'
    result = render(html('<{Navbar} logo_src={LOGO_SRC} />'), container)

    expected = '<nav><img src="logo.png"/></nav>'
    return expected, result
