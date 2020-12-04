from typing import Callable, Type, TypeVar

protocol = TypeVar("protocol")


def adherent(
    c: Callable[[], protocol]
) -> Callable[[Type[protocol]], Type[protocol]]:
    def decor(input_value: Type[protocol]) -> Type[protocol]:
        return input_value

    return decor
