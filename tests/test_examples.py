import pytest

from examples.pluggable import (
    hello_world,
    hello_children,
    hello_app,
    context,
    custom_context,
    subcomponents,
)

from examples.protocols import (
    protocols_hello_logo,
    logo_protocol,
    adherent,
)


@pytest.mark.parametrize(
    'target',
    [
        hello_world,
        hello_children,
        hello_app,
        context,
        custom_context,
        subcomponents,
        protocols_hello_logo,
        logo_protocol,
        adherent,
    ],
)
def test_examples(target):
    expected, actual = target.test()
    assert expected == actual
