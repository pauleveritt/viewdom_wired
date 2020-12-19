from dataclasses import dataclass
from typing import Tuple

import pytest
from viewdom.h import html
from wired.dataclasses import factory, register_dataclass
from wired_injector import InjectorRegistry
from wired_injector.operators import Context, Attr, Get

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
    name: Annotated[
        str,
        Context(),
        Attr('name'),
    ]
    greeting: Annotated[
        str,
        Get(Settings),
        Attr('greeting'),
    ]

    def __call__(self):
        return html('<h1>{self.greeting} {self.person}, {self.name}</h1>')


@pytest.fixture
def registry() -> InjectorRegistry:
    registry = InjectorRegistry()
    registry.scan()
    register_dataclass(registry, Settings)
    return registry


@component(for_=Heading, context=SecondContext)
@dataclass
class SecondHeading:
    person: str
    name: Annotated[
        str,
        Context(),
        Attr('name'),
    ]
    greeting: Annotated[
        str,
        Get(Settings),
        Attr('greeting'),
    ]

    def __call__(self):
        return html(
            '''
        <h1>{self.greeting} {self.person}... {self.name}</h1>
        '''
        )


def test_wired_renderer_first(registry: InjectorRegistry):
    container = registry.create_injectable_container(context=FirstContext())
    expected = '<h1>Hello World, First Context</h1>'
    actual = render(html('<{Heading} person="World"/>'), container)
    assert expected == actual


def test_wired_renderer_second(registry: InjectorRegistry):
    container = registry.create_injectable_container(context=SecondContext())
    expected = '<h1>Hello World... Second Context</h1>'
    actual = render(html('<{Heading} person="World"/>'), container)
    assert expected == actual


def test_wired_renderer_children(registry: InjectorRegistry):
    @dataclass
    class Heading2:
        children: str
        name: str = 'Hello'

        def __call__(self):
            return html('<h1>{self.name}</h1><div>{self.children}</div>')

    registry = InjectorRegistry()
    registry.register_injectable(Heading, Heading2, use_props=True)
    container = registry.create_injectable_container()
    expected = '<h1>Hello</h1><div>Child</div>'
    actual = render(html('<{Heading}>Child</>'), container=container)
    assert expected == actual


def test_wired_renderer_generics(registry: InjectorRegistry):
    """ Tolerate usage of PEP 484 generics on type hints """

    @dataclass
    class LocalHeading:
        names: Tuple[str, ...] = ('Name 1',)

        def __call__(self):
            name_one = self.names[0]  # noqa: F841
            return html('<h1>{name_one}</h1>')

    container = registry.create_injectable_container()
    registry.register_injectable(LocalHeading, LocalHeading, use_props=True)
    expected = '<h1>Name 1</h1>'
    actual = render(html('<{LocalHeading}/>'), container)
    assert expected == actual
