"""
Pluggable application

This what a pluggable application will provide, to be used by plugins
and by sites. At the moment it is just the registry.
"""

from wired import ServiceRegistry

from viewdom_wired import register_component


def make_app(component) -> ServiceRegistry:
    """ At startup, make a registry and register components """

    registry = ServiceRegistry()
    register_component(registry, component)
    return registry
