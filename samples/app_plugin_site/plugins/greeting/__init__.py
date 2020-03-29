"""

A plugin that can be installed with pip and then register its components.

"""
from wired import ServiceRegistry

from viewdom_wired import register_component
from .greeting import Greeting


def setup(registry: ServiceRegistry):
    # Do any startup-time setup, such as registering this
    # package's known components
    register_component(registry, Greeting)
