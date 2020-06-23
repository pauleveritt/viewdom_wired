"""
A pluggable app that can be installed and used.

The features in this app would be grafted into
"""

from dataclasses import dataclass, field
from types import ModuleType
from typing import Optional, Type

from venusian import Scanner
from wired import ServiceRegistry

from viewdom_wired import render


@dataclass
class App:
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)

    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

    def setup(self, module: ModuleType):
        """ Call a plugin's setup function """

        s = getattr(module, 'wired_setup')
        s(self)

    def render(self, vdom, context=Optional[Type]) -> str:
        """ Render a template in a container """

        container = self.registry.create_container(context=context)
        return render(vdom, container)
