"""
A pluggable app that can be installed and can register plugins.
"""

from dataclasses import dataclass, field

from venusian import Scanner
from wired import ServiceRegistry

from viewdom_wired import render


@dataclass
class PunctuationCharacter:
    """ A configurable symbol to use in punctuation """

    symbol: str = '!'


@dataclass
class App:
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)
    scanner: Scanner = field(init=False)

    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

        # Register a singleton for the punctuation character
        self.registry.register_singleton(
            PunctuationCharacter(),
            PunctuationCharacter
        )

    def setup(self, module):
        """ Call a plugin's setup function """

        s = getattr(module, 'setup')
        s(self)

    def render(self, vdom) -> str:
        """ Render a template in a container """

        container = self.registry.create_container()
        return render(vdom, container)
