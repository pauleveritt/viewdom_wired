# viewdom_wired: Container and DI for ``viewdom``

*Pluggability for Templates and Components*

Let's say you share some nice components.
You want them to work in different systems: Sphinx, Pelican, Flask, etc.
You also want to make it easy to extend or customize without having to fork.

`viewdom_wired` brings pluggability and flexibility to [viewdom](https://viewdom.readthedocs.io/en/latest/) templates and components.
With dependency injection and containers from [wired](https://wired.readthedocs.io/en/latest/>), the components in your {doc}`pluggable apps <./pluggable>` are now swappable, easier to write and test, and less brittle.

:::{note}

  This is for people who want to make or consume a pluggable system.
  If that's not you, then it's unneeded complexity/magic.
:::

## Installation

For Python 3.7+:

```bash
$ pip install viewdom_wired
```

For Python 3.6, you'll need the `dataclasses` backport.

## Minimum Example

Let's write a `Greeting` component.
It expects to be passed a `first_name`:

```{literalinclude} ../examples/index/hello_component/components.py
---
start-at: component(
---
```

You can then render a template which passes in `first_name` as a string:

```{literalinclude} ../examples/index/hello_component/app.py
---
start-at: render(
end-at: render(
---
```

Don't want to pass data down long component trees?
Tell the injector to use a pipeline to get it:

```{literalinclude} ../examples/index/hello_settings/components.py
---
start-at: Annotated[
end-at: Annotated[
---
```

Want to use that, but some of the time, manually pass in a prop to the component to override the injected value?
Do so, and use an expression as the prop value:

```{literalinclude} ../examples/index/prop_override/app.py
---
start-at: first_name =
end-at: render(
---
```

## How It Works

`viewdom_wired` changes the `viewdom` rendering to use the `wired_injector`.
It transparently wires up an `InjectorContainer` for the rendering, provides a `@component` decorator to turn on `use_props`, and pass long `system_props` such as `children`, `parent_component`, and whatever you pass into the render.


```{toctree}
---
hidden: true
---
pluggable
protocols
who
what
why
future
```
