from dataclasses import dataclass

import pytest
from wired import ServiceRegistry
from wired.dataclasses import factory, register_dataclass


@factory()
@dataclass
class Settings:
    greeting: str = 'Hello'


@pytest.fixture
def registry() -> ServiceRegistry:
    import sys
    from venusian import Scanner

    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    current_module = sys.modules[__name__]
    scanner.scan(current_module)
    register_dataclass(registry, Settings)
    return registry
