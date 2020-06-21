"""
A plugin that can be installed with pip and then register its components.
"""
from dataclasses import dataclass

from viewdom import html, VDOM
from wired import ServiceRegistry

from viewdom_wired import register_component


@dataclass
class Greeting:
    name: str = 'viewdom_wired'

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>')


def wired_setup(registry: ServiceRegistry):
    # Do any startup-time setup, such as registering this
    # package's known components
    register_component(registry, Greeting)
