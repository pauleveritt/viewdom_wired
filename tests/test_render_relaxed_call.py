"""
The component renderer uses a variation of wired's dataclass dependency
injector. Write some tests that cover policies.

"""
from dataclasses import dataclass

from viewdom import html, VDOM
from wired.dataclasses import injected, Context

from viewdom_wired import register_component
from viewdom_wired.render import make_component


class Person:
    """ A marker class """
    pass


def test_str_default_value(registry, container):
    """ Simple type (str) and has a default """

    @dataclass
    class TestPerson:
        name: str = 'default'

        def __call__(self) -> VDOM:
            return html('<div>{self.name}</div>')

    register_component(registry, for_=Person, target=TestPerson)
    person = make_component(container, Person)

    assert 'default' == person.name


def test_str_prop(registry, container):
    """ Simple type (str) with passed-in value """

    @dataclass
    class TestPerson:
        name: str = 'default'

        def __call__(self) -> VDOM:
            return html('<div>{self.name}</div>')

    register_component(registry, for_=Person, target=TestPerson)
    person = make_component(container, Person, name='passed in')

    assert 'passed in' == person.name


def test_context(registry):
    """ Use the type-hint to inject the context """

    @dataclass
    class Customer:
        name: str = 'Some Customer'

    @dataclass
    class TestPerson:
        customer: Context

        def __call__(self) -> VDOM:
            return html('<div>{self.customer.name}</div>')

    container = registry.create_container(context=Customer())
    register_component(registry, for_=Person, target=TestPerson)
    person = make_component(container, Person)

    assert 'Some Customer' == person.customer.name


def test_injected_attr(registry):
    """ Used ``injected`` to get the context and grab an attr """

    @dataclass
    class Customer:
        name: str = 'Some Customer'

    @dataclass
    class TestPerson:
        name: str = injected(Context, attr='name')

        def __call__(self) -> VDOM:
            return html('<div>{self.name}</div>')

    container = registry.create_container(context=Customer())
    register_component(registry, for_=Person, target=TestPerson)
    person = make_component(container, Person)

    assert 'Some Customer' == person.name


