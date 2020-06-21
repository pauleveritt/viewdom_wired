from dataclasses import dataclass, field
from types import ModuleType
from typing import Optional, Type

from venusian import Scanner
from wired import ServiceRegistry

from viewdom_wired import render
from . import components  # noqa


@dataclass
class App:
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)

    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

        # Register the built-in components
        self.scanner.scan(components)

    def setup(self, module: ModuleType):
        """ Call a plugin's setup function """

        s = getattr(module, 'wired_setup')
        s(self)

    def render(self, vdom, context=Optional[Type]) -> str:
        """ Render a template in a container """

        container = self.registry.create_container(context=context)
        return render(vdom, container)
