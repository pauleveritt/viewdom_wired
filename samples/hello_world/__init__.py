"""

A simple example using (a) a pluggable app and (b) some known
components.

All 3 roles are in one file: pluggable app, plugins, a site using both.

All 3 parts are done on every invokation:

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
        return html('''<h1>Hello {self.name}</h1>''')


def main() -> str:
    registry = ServiceRegistry()
    register_component(registry, Greeting)
    container = registry.create_container()
    return render(html('''<{Greeting}/>'''), container)
