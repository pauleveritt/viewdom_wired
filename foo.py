"""
Protocols and "adherent" but as a register_component function.

The ``@adherent`` decorator from Glyph gets mypy and protocols
around the ``@dataclass`` decorator problem. But it gets pretty
verbose. And seems to suffer from a ``frozen=True`` problem.

Also, it isn't clear whether ``DefaultPerson(Person)`` will be
the best way to indicate "implements" to tooling: PyCharm, static
typing, mypy plugins, etc.

Let's try putting the benefits of ``@adherent`` but to a
``register_component`` function which is protocol-centric.
"""
from typing import Protocol, Callable


class Person(Protocol):
    name: str


class FrenchPerson(Person):
    name: str


def register_component(
        registry: int,
        target: Callable,
        for_: Protocol
) -> None:
    return None


if __name__ == '__main__':
    register_component(9, Person, FrenchPerson)
