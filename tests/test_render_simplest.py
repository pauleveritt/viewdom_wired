from dataclasses import dataclass, field
from typing import List

from viewdom.h import html, VDOM
from wired import ServiceRegistry

from viewdom_wired import register_component


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
        full_name = ' '.join(self.full_name)
        return html('<div>{full_name}</div>')


def test_wired_renderer_simplest_nocontainer(registry: ServiceRegistry):
    from viewdom.h import render
    instance = Heading(name='No Wired')
    expected = '<h1>No Wired</h1>'
    actual = render(instance())
    assert expected == actual


def test_wired_renderer_simplest_container(registry: ServiceRegistry):
    from viewdom_wired import render
    container = registry.create_container()
    register_component(registry, Heading)
    expected = '<h1>Hello</h1>'
    actual = render(html('''<{Heading}/>'''), container)
    assert expected == actual


def test_wired_renderer_simplest_propoverride(registry: ServiceRegistry):
    from viewdom_wired import render
    container = registry.create_container()
    register_component(registry, Heading)
    expected = '<h1>Override</h1>'
    actual = render(html('''<{Heading} name="Override"/>'''), container)
    assert expected == actual


def test_wired_renderer_simplest_init_false(registry: ServiceRegistry):
    from viewdom_wired import render
    container = registry.create_container()
    register_component(registry, Person)
    expected = '<div>Paul Everitt</div>'
    actual = render(html('''<{Person} first_name="Paul" last_name="Everitt"/>'''), container)
    assert expected == actual
