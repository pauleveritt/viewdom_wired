"""
A simple example using (a) a pluggable app and (b) some known
components.

All 3 roles are in one file: pluggable app, plugins, a site using both.

All 3 parts are done on every invocation:

- Make a registry
- Register the components
- Make a container
- Render a template
"""

from dataclasses import dataclass

from viewdom import html
from wired import ServiceRegistry

from viewdom_wired import render, register_component


@dataclass
class Greeting:
    name: str = 'viewdom_wired'

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')


def site_startup() -> ServiceRegistry:
    # Make a instance when the site starts up
    registry = ServiceRegistry()
    register_component(registry, Greeting)
    return registry


def main() -> str:
    registry = site_startup()
    # Process a request and return a response
    container = registry.create_container()
    return render(html('<{Greeting}/>'), container)
