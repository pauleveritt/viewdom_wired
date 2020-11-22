"""
A pluggable app that can be installed and used.

This would represent something like Sphinx, Flask, etc.
"""
from dataclasses import dataclass, field
from typing import Type

from wired import ServiceRegistry
from wired_injector.decorators import register_injectable


@dataclass
class App:
    registry: ServiceRegistry = field(default_factory=ServiceRegistry)

    def setup(self, component: Type):
        """ Add a component to the registry """
        register_injectable(self.registry, component)
