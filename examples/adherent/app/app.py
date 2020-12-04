from dataclasses import dataclass

from venusian import Scanner

from . import components
from ...context.app import App as BaseApp


@dataclass
class App(BaseApp):
    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

        # Register the built-in components
        self.scanner.scan(components)
