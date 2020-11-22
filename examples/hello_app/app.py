"""
Pluggable application

This what a pluggable application will provide, to be used by plugins
and by sites. At the moment it is just the registry.
"""

from wired import ServiceRegistry
from wired_injector.decorators import register_injectable


def make_app(component) -> ServiceRegistry:
    """ At startup, make a registry and register components """

    registry = ServiceRegistry()
    register_injectable(registry, component)
    return registry
