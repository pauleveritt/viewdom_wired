"""
A pluggable app that can be installed and can register decorator-based
plugins.
"""

from dataclasses import dataclass, field
from types import ModuleType

from venusian import Scanner
from viewdom import VDOM
from wired import ServiceRegistry

from viewdom_wired import render


@dataclass
class App:
    """ A pluggable app with a registry and a decorator scanner """
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)

    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

    def setup(self, module: ModuleType):
        """ Call a plugin's setup function """

        s = getattr(module, 'wired_setup')
        s(self)

    def render(self, vdom: VDOM) -> str:
        """ Make a container and render a template in it """

        container = self.registry.create_container()
        return render(vdom, container)
