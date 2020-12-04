"""
A pluggable app that can be installed and can register plugins.
"""

from dataclasses import dataclass

from venusian import Scanner

from ...app_decorators_render.app import App as BaseApp


@dataclass
class PunctuationCharacter:
    """ A configurable symbol to use in punctuation """

    symbol: str = '!'


@dataclass
class App(BaseApp):
    def __post_init__(self):
        self.scanner = Scanner(registry=self.registry)

        # Register a singleton for the punctuation character
        self.registry.register_singleton(
            PunctuationCharacter(), PunctuationCharacter
        )
