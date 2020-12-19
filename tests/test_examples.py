import pytest

from examples.index import (
    hello_component,
    hello_settings,
    prop_override,
)
from examples.pluggable import (
    hello_world,
    hello_children,
    hello_app,
    context,
    custom_context,
    subcomponents,
)

from examples.protocols import (
    hello_logo,
    logo_protocol,
    adherent,
)


@pytest.mark.parametrize(
    'target',
    [
        hello_component,
        hello_settings,
        prop_override,
        hello_world,
        hello_children,
        hello_app,
        context,
        custom_context,
        subcomponents,
        hello_logo,
        logo_protocol,
        adherent,
    ],
)
def test_examples(target):
    expected, actual = target.test()
    assert expected == actual
