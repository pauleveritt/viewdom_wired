"""
Sample application

This what a pluggable framework or application will provide,
to be used by plugins and by sites.
"""

from wired import ServiceRegistry

from viewdom_wired import register_component


def make_app(component) -> ServiceRegistry:
    """ At startup, make a registry and register components """

    registry = ServiceRegistry()
    register_component(registry, component)
    return registry
