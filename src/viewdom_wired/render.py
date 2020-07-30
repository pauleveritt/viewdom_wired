from dataclasses import fields, Field, MISSING
from typing import get_type_hints

from viewdom import Context
from viewdom.h import flatten, escape, encode_prop, VDOMNode
from wired import ServiceContainer
from wired.dataclasses import Context as WiredContext


def make_component(container: ServiceContainer, callable_, children=None, parent_component=None, **kwargs):
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

        full_field: Field = fields_mapping[field_name]

        # ----  Special cases to bail out early on
        # Field has init=False which means, don't initialize
        if full_field.init is False:
            continue

        # Field named "children" which reflects the
        # possibly-existing child nodes.
        if field_name == 'children':
            if children:
                # We were "passed" some children as subnodes
                args[field_name] = children
            else:
                # Better have something as a field default
                args[field_name] = full_field.default
            continue

        # Another name-based special case..."parent_children" means to get
        # the value from the parent component's default field value for
        # "parent_children". Used to implement Jinja2-style blocks.
        if field_name == 'parent_children':
            # We have to use fields on the parent to get at the default value
            parent_fields = fields(parent_component)

            # Get the first field that matches the <{Block} name="fieldname"> name
            parent_field = next(f for f in parent_fields if f.name == props['name'])

            # Now that you have the correct field on the parent's dataclass, get its
            # default value
            parent_value = parent_field.default
            args['parent_children'] = parent_value
            continue

        # Next-highest precedence: this field occurs in the passed-in
        # props. Check there first.
        if props and field_name in props:
            prop_value = props[field_name]
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

        # Is the field_type a generic from typing? For example, Tuple[str, ...]
        import typing
        from inspect import getmodule
        if getmodule(field_type) is typing:
            # We expect this case to have a default value
            args[field_name] = getattr(full_field, 'default', None)
            continue

        # Now the general case, something like url: Url
        try:
            field_value = container.get(field_type)
            args[field_name] = field_value
        except (TypeError, LookupError):
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
            elif hasattr(target, '__post_init__'):
                continue
            else:
                msg = f'No default value on field {field_name}'
                raise LookupError(msg)

    # Now construct an instance of the target dataclass
    component = target(**args)
    return component


def relaxed_call(container: ServiceContainer, callable_, children=None, parent_component=None, **kwargs):
    """ Make a component instance then call its __call__, returning a VDOM """
    component = make_component(container, callable_, children=children, parent_component=parent_component, **kwargs)
    return component


def render(value, container: ServiceContainer, **kwargs):
    return "".join(render_gen(Context(value, **kwargs), container=container, children=None, parent_component=None))


def render_gen(value, container: ServiceContainer, children=None, parent_component=None):
    for item in flatten(value):
        if isinstance(item, VDOMNode):
            tag, props, children = item.tag, item.props, item.children
            if callable(tag):
                component = relaxed_call(
                    container,
                    tag,
                    children=children,
                    parent_component=parent_component,
                    **props
                )
                parent_component = component
                yield from render_gen(
                    component(),
                    container,
                    children,
                    parent_component
                )
                continue

            yield f"<{escape(tag)}"
            if props:
                yield f" {' '.join(encode_prop(k, v) for (k, v) in props.items())}"

            if children:
                yield ">"
                yield from render_gen(children, container, parent_component=parent_component)
                yield f'</{escape(tag)}>'
            else:
                yield f'/>'
        elif item not in (True, False, None):
            yield escape(item)
