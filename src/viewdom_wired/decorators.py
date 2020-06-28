from inspect import getmro
from typing import TypeVar, Callable, Optional, Any, Type

from venusian import Scanner, attach
from wired import ServiceContainer, ServiceRegistry

protocol = TypeVar("protocol")


def register_component(
        registry: ServiceRegistry,
        for_: Callable,
        target: Callable = None,
        context: Optional[Any] = None
):
    """ Imperative form of the component decorator """

    def component_factory(container: ServiceContainer):
        return target if target else for_

    registry.register_factory(
        component_factory, for_, context=context
    )


class component:
    def __init__(self, for_: type = None, context: Type = None):
        self.for_ = for_
        self.context = context

    def __call__(self, wrapped):
        def callback(scanner: Scanner, name: str, cls):
            for_ = self.for_ if self.for_ else cls
            registry: ServiceRegistry = getattr(scanner, 'registry')

            register_component(
                registry,
                for_,
                target=cls,
                context=self.context,
            )

        attach(wrapped, callback, category='wired_component')
        return wrapped


def adherent(c: Callable[[], protocol]) -> Callable[[Type[protocol]], Type[protocol]]:
    def decor(input_value: Type[protocol]) -> Type[protocol]:
        return input_value

    return decor


class component2:
    def __init__(self, for_: type = None, context: Type = None):
        self.for_ = for_
        self.context = context

    def __call__(self, wrapped):
        # Protocol support: If first base class listed is a Protocol,
        # then use it as the for_, if for_ is None.
        if self.for_ is None:
            bases = getmro(wrapped)
            if bases:
                # The target has some base classes, check the first to
                # see if it is a protocol
                first_base = getmro(wrapped)[1]
                if getattr(first_base, '_is_protocol', False):
                    # Replace for_ with this protocol
                    self.for_ = first_base

        def callback(scanner: Scanner, name: str, cls):
            for_ = self.for_ if self.for_ else cls
            registry: ServiceRegistry = getattr(scanner, 'registry')

            register_component(
                registry,
                for_,
                target=cls,
                context=self.context,
            )

        attach(wrapped, callback, category='wired_component')
        return wrapped
