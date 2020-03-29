from dataclasses import dataclass

from wired import ServiceRegistry

from viewdom.h import html
from viewdom_wired import render, component, register_component


@component()
@dataclass
class Heading:
    name: str = 'Hello'

    def __call__(self):
        return html('''<h1>{self.name}</h1>''')


def test_wired_renderer_simplest_nocontainer(registry: ServiceRegistry):
    from viewdom.h import render
    instance = Heading(name='No Wired')
    expected = '<h1>No Wired</h1>'
    actual = render(instance())
    assert expected == actual


def test_wired_renderer_simplest_container(registry: ServiceRegistry):
    container = registry.create_container()
    register_component(registry, Heading)
    expected = '<h1>Hello</h1>'
    actual = render(html('''<{Heading}/>'''), container)
    assert expected == actual


def test_wired_renderer_simplest_propoverride(registry: ServiceRegistry):
    container = registry.create_container()
    register_component(registry, Heading)
    expected = '<h1>Override</h1>'
    actual = render(html('''<{Heading} name="Override"/>'''), container)
    assert expected == actual
