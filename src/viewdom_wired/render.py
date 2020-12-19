from viewdom import Context
from viewdom.h import flatten, escape, encode_prop, VDOMNode, VOIDS
from wired_injector.registry import InjectorContainer


def relaxed_call(
    container: InjectorContainer,
    callable_,
    children=None,
    parent_component=None,
    **kwargs,
):
    """ Make a component instance then call its __call__, returning a VDOM """

    # In the component rendering, the context is always the
    # container's context.
    context = container.context
    system_props = dict(children=children, parent_component=parent_component)
    component = container.inject(
        callable_, context=context, system_props=system_props, **kwargs
    )
    return component


def render(value, container: InjectorContainer, **kwargs):
    return "".join(
        render_gen(
            Context(value, **kwargs),
            container=container,
            children=None,
            parent_component=None,
        )
    )


def render_gen(
    value, container: InjectorContainer, children=None, parent_component=None
):
    for item in flatten(value):
        if isinstance(item, VDOMNode):
            tag, props, children = item.tag, item.props, item.children
            if callable(tag):
                component = relaxed_call(
                    container,
                    tag,
                    children=children,
                    parent_component=parent_component,
                    **props,
                )
                parent_component = component
                yield from render_gen(
                    component(), container, children, parent_component
                )
                continue

            yield f"<{escape(tag)}"
            if props:
                pi = props.items()
                yield f" {' '.join(encode_prop(k, v) for (k, v) in pi)}"

            if children:
                yield ">"
                yield from render_gen(
                    children, container, parent_component=parent_component
                )
                yield f'</{escape(tag)}>'
            elif tag.lower() in VOIDS:
                yield '/>'
            else:
                yield f'></{tag}>'
        elif item not in (True, False, None):
            yield escape(item)
