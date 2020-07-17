"""
A component that can have nested nodes passed to it via injection.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from wired import ServiceRegistry

from viewdom_wired import render, register_component


@dataclass
class Greeting:
    """ A simple component, passed one argument """
    name: str = 'viewdom_wired'
    children: VDOM = html('<span>Default</span>')

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>{self.children}')


def site_startup() -> ServiceRegistry:
    """ At startup, make a registry and register a component """

    registry = ServiceRegistry()
    register_component(registry, Greeting)
    return registry


def main() -> str:
    """ Combine startup with processing a request """

    registry = site_startup()
    container = registry.create_container()
    return render(html('<{Greeting}><span>Children</span><//>'), container)
