"""
The component renderer uses a variation of wired's dataclass dependency
injector via use_props. Write some tests that cover policies.

"""
from dataclasses import dataclass

import pytest
from wired_injector import InjectorRegistry
from wired_injector.operators import Context, Attr

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore


class BaseHeading:
    """ A marker class for an injectable to register against """


@dataclass
class Customer:
    name: str = 'Some Customer'


@pytest.fixture
def registry() -> InjectorRegistry:
    r = InjectorRegistry()
    return r


def test_str_default_value(registry):
    """ Simple type (str) and has a default """

    @dataclass
    class Heading:
        title: str = 'Heading'

    registry.register_injectable(
        for_=BaseHeading,
        target=Heading,
        use_props=True,
    )
    container = registry.create_injectable_container()
    heading: Heading = container.get(BaseHeading)
    assert 'Heading' == heading.title


def test_str_props(registry):
    """ Simple type (str) with passed-in value as props """

    @dataclass
    class Heading:
        title: str = 'Heading'

    registry.register_injectable(
        for_=BaseHeading,
        target=Heading,
        use_props=True,
    )
    container = registry.create_injectable_container()
    heading: Heading = container.inject(BaseHeading, title='passed in')
    assert 'passed in' == heading.title


def test_context(registry):
    """ Use the type-hint to inject the context """

    @dataclass
    class Heading:
        customer: Annotated[
            Customer,
            Context(),
        ]

    registry.register_injectable(
        for_=BaseHeading,
        target=Heading,
        context=Customer,
        use_props=True,
    )
    context = Customer()
    container = registry.create_injectable_container(context=context)
    heading: Heading = container.inject(BaseHeading, context=context)
    assert 'Some Customer' == heading.customer.name


def test_injected_attr(registry):
    """ Used ``injected`` to get the context and grab an attr """

    @dataclass
    class Heading:
        title: Annotated[
            str,
            Context(),
            Attr('name'),
        ]

    registry.register_injectable(
        for_=BaseHeading,
        target=Heading,
        use_props=True,
    )
    context = Customer()
    container = registry.create_injectable_container(
        context=context,
    )
    heading: Heading = container.inject(BaseHeading)
    assert 'Some Customer' == heading.title
