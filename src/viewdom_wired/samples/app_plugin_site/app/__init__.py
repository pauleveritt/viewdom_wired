"""
A pluggable app that can be installed and used.

This would represent something like Sphinx, Flask, etc.
"""

from wired import ServiceRegistry


def make_app() -> ServiceRegistry:
    """ At startup, make a registry """

    registry = ServiceRegistry()
    return registry
