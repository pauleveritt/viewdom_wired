"""
A simple example using (a) a pluggable app and (b) a known
component.

All 3 roles are in one file: pluggable app, plugins, a site using both.

All 3 parts are done on every invocation:

- Make a registry
- Register the components
- Make a container
- Render a template
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from wired import ServiceRegistry
from wired_injector.decorators import register_injectable

from viewdom_wired import render


@dataclass
class Greeting:
    """ A simple component, passed one argument """

    name: str = 'viewdom_wired'

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>')


def site_startup() -> ServiceRegistry:
    """ At startup, make a registry and register a component """

    registry = ServiceRegistry()
    register_injectable(registry, Greeting)
    return registry


def main() -> str:
    """ Combine startup with processing a request """

    registry = site_startup()
    container = registry.create_container()
    return render(html('<{Greeting}/>'), container)


expected = '<h1>Hello viewdom_wired</h1>'
