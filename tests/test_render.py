from dataclasses import dataclass
from typing import Any, Sequence

import pytest
from wired import ServiceRegistry
from wired.dataclasses import injected, Context, factory, register_dataclass

from viewdom.h import html
from viewdom_wired import render, component, register_component


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


def test_wired_renderer_children(registry: ServiceRegistry):
    @dataclass
    class Heading2:
        children: Sequence
        name: str = 'Hello'

        def __call__(self):
            return html('''<h1>{self.name}</h1><div>{self.children}</div>''')

    registry = ServiceRegistry()
    register_component(registry, Heading, Heading2)
    container = registry.create_container()
    expected = '<h1>Hello</h1><div>Child</div>'
    actual = render(html('''<{Heading}>Child<//>'''), container)
    assert expected == actual
