"""

Test usage of wired and components via decorators instead of
imperative.

More cumbersome (due to scanner) to copy around so placed into a
single test.

"""
from dataclasses import dataclass

import pytest
from viewdom.h import html
from wired import ServiceRegistry
from wired.dataclasses import injected, Context, factory, register_dataclass

from viewdom_wired import render, component


class FirstContext:
    def __init__(self):
        self.name = 'First Context'


class SecondContext:
    def __init__(self):
        self.name = 'Second Context'


@factory()
@dataclass
class Settings:
    greeting: str = 'Hello'


@component()
@dataclass
class Heading:
    person: str
    name: str = injected(Context, attr='name')
    greeting: str = injected(Settings, attr='greeting')

    def __call__(self):
        return html('''<h1>{self.greeting} {self.person}, {self.name}</h1>''')


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


@component(for_=Heading, context=SecondContext)
@dataclass
class SecondHeading:
    person: str
    name: str = injected(Context, attr='name')
    greeting: str = injected(Settings, attr='greeting')

    def __call__(self):
        return html('''<h1>{self.greeting} {self.person}... {self.name}</h1>''')


def test_wired_renderer_first(registry: ServiceRegistry):
    container = registry.create_container(context=FirstContext())
    expected = '<h1>Hello World, First Context</h1>'
    actual = render(html('''<{Heading} person="World"/>'''), container)
    assert expected == actual


def test_wired_renderer_second(registry: ServiceRegistry):
    container = registry.create_container(context=SecondContext())
    expected = '<h1>Hello World... Second Context</h1>'
    actual = render(html('''<{Heading} person="World"/>'''), container)
    assert expected == actual
