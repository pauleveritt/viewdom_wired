from dataclasses import fields, Field, MISSING
from typing import get_type_hints, Callable, Optional, Any, Type

from venusian import Scanner, attach
from viewdom import Context, VDOM
from viewdom.h import flatten, escape, encode_prop
from wired import ServiceContainer, ServiceRegistry
from wired.dataclasses import Context as WiredContext


def register_component(
        registry: ServiceRegistry,
        for_: Callable,
        target: Callable=None,
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


def relaxed_call(container: ServiceContainer, callable_, **kwargs):
    context = container.context
    target = container.get(callable_)
    props = kwargs

    # Make the args dict that we will construct dataclass with
    args = {}

    # Iterate through the dataclass fields
    # Because fields() gives a string for the type, instead of the
    # actual type, let's get a mapping of field name -> field type
    fields_mapping = {f.name: f for f in fields(target)}

    # Iterate through the dataclass fields
    for field_name, field_type in get_type_hints(target).items():

        # Highest precedence: this field occurs in the passed-in
        # props. Check there first.
        if props and field_name in props:
            args[field_name] = props[field_name]
            continue

        # Doing this style of bailing out quickly for performance
        # reasons. Don't want to keep doing "if", though it
        # means some repetitions.
        if field_type is ServiceContainer:
            args[field_name] = container
            continue

        if field_type == WiredContext:
            args[field_name] = context
            continue

        # See if this field is using the injectable field, e.g.
        # url: str = injected(Url, attr='value')
        full_field: Field = fields_mapping[field_name]
        if full_field.metadata.get('injected', False):
            injected_info = full_field.metadata['injected']
            injected_attr = injected_info.get('attr')
            injected_type = injected_info['type_']
            injected_name = injected_info.get('name')

            # Another special case: if asked to inject WiredContext or
            # ServiceContainer, consider it like a sentinel and return it.
            if injected_type is WiredContext:
                injected_target = context
            elif injected_type is ServiceContainer:
                injected_target = container
            else:
                # Ask the registry for one of these
                injected_target = container.get(injected_type)

            # If attr is used, get specified attribute off that instance
            if injected_attr:
                field_value = getattr(injected_target, injected_attr)
            else:
                field_value = injected_target
            args[field_name] = field_value
            continue

        # Now the general case, something like url: Url
        try:
            field_value = container.get(field_type)
            args[field_name] = field_value
        except TypeError:
            # Seems that wired, when looking up str, gives:
            #   TypeError: can't set attributes of bui...sion type 'str'
            # We will use that to our advantage to look for a dataclass
            # field default value.
            field_default = getattr(full_field, 'default', None)
            if field_default is not MISSING:
                args[field_name] = field_default
                continue
            elif full_field.init is False:
                # Expect a __post_init__ that assigns this value
                if not hasattr(target, '__post_init__'):
                    m = 'has init=False but no __post_init__'
                    msg = f'Field "{field_name}" {m}'
                    raise LookupError(msg)
                continue
            else:
                msg = f'No default value on field {field_name}'
                raise LookupError(msg)
        except LookupError:
            # Give up and work around ``wired`` unhelpful exception
            # by adding some context information.

            # Note that a dataclass with ``__post_init__`` might still
            # do some construction. Only do this next part if there's
            # no __post_init__
            if not hasattr(target, '__post_init__'):
                m = 'Injector failed for'
                msg = f'{m} {field_name} on {target.__name__}'
                raise LookupError(msg)

    # Now construct an instance of the target dataclass
    component = target(**args)
    return component()


def render(value, container: ServiceContainer, **kwargs):
    return "".join(render_gen(Context(value, **kwargs), container=container))


def render_gen(value, container: ServiceContainer):
    for item in flatten(value):
        if isinstance(item, VDOM):
            tag, props, children = item.tag, item.props, item.children
            if callable(tag):
                yield from render_gen(relaxed_call(container, tag, children=children, **props), container)
                continue

            yield f"<{escape(tag)}"
            if props:
                yield f" {' '.join(encode_prop(k, v) for (k, v) in props.items())}"

            if children:
                yield ">"
                yield from render_gen(children, container)
                yield f'</{escape(tag)}>'
            else:
                yield f'/>'
        elif item not in (True, False, None):
            yield escape(item)
