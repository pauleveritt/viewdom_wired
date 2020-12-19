"""

Test usage of wired and components via decorators instead of
imperative.

More cumbersome (due to scanner) to copy around so placed into a
single test.

"""
from dataclasses import dataclass

import pytest
from viewdom.h import html
from wired.dataclasses import factory
from wired_injector import InjectorRegistry
from wired_injector.operators import Attr, Context, Get

from viewdom_wired import render, component

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore


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
    name: Annotated[str, Context(), Attr('name')]
    greeting: Annotated[str, Get(Settings), Attr('greeting')]

    def __call__(self):
        return html('''<h1>{self.greeting} {self.person}, {self.name}</h1>''')


@pytest.fixture
def registry() -> InjectorRegistry:
    registry = InjectorRegistry()
    registry.scan()
    return registry


@component(for_=Heading, context=SecondContext)
@dataclass
class SecondHeading:
    person: str
    name: Annotated[str, Context(), Attr('name')]
    greeting: Annotated[str, Get(Settings), Attr('greeting')]

    def __call__(self):
        return html(
            '''
        <h1>{self.greeting} {self.person}... {self.name}</h1>
        '''
        )


def test_wired_renderer_first(registry: InjectorRegistry):
    container = registry.create_injectable_container(context=FirstContext())
    expected = '<h1>Hello World, First Context</h1>'
    actual = render(html('''<{Heading} person="World"/>'''), container)
    assert expected == actual


def test_wired_renderer_second(registry: InjectorRegistry):
    container = registry.create_injectable_container(context=SecondContext())
    expected = '<h1>Hello World... Second Context</h1>'
    actual = render(html('''<{Heading} person="World"/>'''), container)
    assert expected == actual
