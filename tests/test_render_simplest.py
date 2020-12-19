from dataclasses import dataclass, field
from typing import List

import pytest
from viewdom.h import html, VDOM, render
from wired_injector import InjectorRegistry


@dataclass
class Heading:
    name: str = 'Hello'

    def __call__(self) -> VDOM:
        return html('''<h1>{self.name}</h1>''')


@dataclass
class Person:
    first_name: str
    last_name: str
    full_name: List[str] = field(init=False)

    def __post_init__(self):
        self.full_name = [self.first_name, self.last_name]

    def __call__(self):
        full_name = ' '.join(self.full_name)  # noqa: F841
        return html('<div>{full_name}</div>')


@pytest.fixture
def registry() -> InjectorRegistry:
    r = InjectorRegistry()
    return r


def test_wired_renderer_simplest_nocontainer():
    instance = Heading(name='No Wired')
    expected = '<h1>No Wired</h1>'
    actual = render(instance())
    assert expected == actual


def test_wired_renderer_simplest_container(registry: InjectorRegistry):
    registry.register_injectable(Heading, Heading)
    container = registry.create_injectable_container()
    expected = '<h1>Hello</h1>'
    actual = render(html('''<{Heading}/>'''), container=container)
    assert expected == actual


def test_wired_renderer_simplest_propoverride(registry: InjectorRegistry):
    registry.register_injectable(Heading, Heading)
    container = registry.create_injectable_container()
    expected = '<h1>Override</h1>'
    actual = render(html('<{Heading} name="Override"/>'), container=container)
    assert expected == actual


def test_wired_renderer_simplest_init_false(registry: InjectorRegistry):
    registry.register_injectable(Person, Person)
    container = registry.create_injectable_container()
    expected = '<div>Paul Everitt</div>'
    actual = render(
        html('<{Person} first_name="Paul" last_name="Everitt"/>'),
        container=container,
    )
    assert expected == actual


def test_wired_renderer_non_void(registry: InjectorRegistry):
    @dataclass
    class NonVoid:
        def __call__(self):
            return html('<i class="icon"></i>')

    registry.register_injectable(NonVoid, NonVoid)
    container = registry.create_injectable_container()
    expected = '<i class="icon"></i>'
    actual = render(html('<{NonVoid} />'), container=container)
    assert expected == actual
