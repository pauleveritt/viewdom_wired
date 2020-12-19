# Pluggable Apps

As discussed in [](./why), `viewdom_wired` is aimed at pluggable apps.
That document briefly explains what the means and why it matters.
Let's take a closer look.

In this document we'll gradually write a pluggable ecosystem which has 3 actors:

- A *pluggable app*, which does something "out of the box" and has some built-in things like components
- A *plugin*, which is written for that pluggable app, and might add *or replace* some of the app's services
- A *site* which installs the pluggable app, some plugins, and might add/replace/override some components

## Pluggable Site

Let's write a basic application using the pluggability ideas in `viewdom_wired`.
We'll start with something very basic and gradually introduce some of the basic ideas.
All of these examples are in the repository's `examples` directory with tests that cover them in the `tests` directory.

## Minimum Pluggable App

We'll start with a pluggable app.
When it starts up, it makes a registry.
It then proceeds to process one or more requests:

```{literalinclude} ../examples/pluggable/hello_world/app.py
---
---
```

For testing purposes, we assign `expected` with what we think will be the result, then return both.

This app is simple: it renders a `Greeting` component that is built-into the app.
Here are the components the pluggable app ships with:

```{literalinclude} ../examples/pluggable/hello_world/components.py
---
start-at: component()
---
```

## Component Children

With [viewdom](viewdom:index) we can take the child nodes in a template and pass it to the component.
The component then asks for -- as a dataclass field, a function argument, a namedtuple field -- a special name of `children`.
This works in `viewdom_wired as well`.

First we see the template where it is used:

```{literalinclude} ../examples/pluggable/hello_children/app.py
---
start-after: container =
end-at: result =
---
```

The component dataclass now has a field with a special name of `children`:

```{literalinclude} ../examples/pluggable/hello_children/components.py
---
start-at: component(
emphasize-lines: 5-5, 8-8
---
```

Why bring this up?
Because it's part of what `viewdom_wired` adds beyond just `viewdom`: a concept of "props" that can be part of the injectable information.
Other injector systems don't have that, and it's (obviously) critical for `viewdom_wired` and components.

## All Three Roles

Of course that's not very real-world.
Let's show a case that splits the three roles: pluggable app, a plugin, and a site that uses both along with local customizations.

First, a pluggable app, which scans for plugins first, then site customizations second (and thus, higher priority).
It gets the list of plugins from the site, which is in control:

```{literalinclude} ../examples/pluggable/hello_app/app.py
---
---
```

Then, a third-party plugin for the app, providing a `Greeting` component that can be used in a site:

```{literalinclude} ../examples/pluggable/hello_app/plugins/greeting.py
---
---
```

Finally, the site itself.
It registers a component which *replaces* the plugin's `Greeting` component.
It also tells the pluggable app what plugins it is using:

```{literalinclude} ../examples/pluggable/hello_app/site.py
---
---
```

One thing that is nice about this: we didn't use subclassing to establish the is-a relationship between `Greeting` and `SiteGreeting`.
Instead, the registration handled this with the `for_` decorator argument.

## Container Context

Components don't have to get all their info from passed-in props.
They can ask the injector to get information for them, for example, from the `wired` container's context.

The app changes, as we want our container created with a `Customer` as context:

```{literalinclude} ../examples/pluggable/context/app.py
---
---
```

Here's a **big** point: the component asks the *injector* to get the *context*.
Thus, the parent components don't have to pass this all the way down.
Moreover, the injector is asked to get a specific attribute off the context, which is nice for two reasons:

- The consumer of this component could pass in a different value, eliminating injection of the value from the context

- The component has a smaller surface area with the outside world, instead of getting the entire context

```{literalinclude} ../examples/pluggable/context/plugins/greeting.py
---
---
```

The site defines different kinds of contexts:

```{literalinclude} ../examples/pluggable/context/site/contexts.py
---
---
```

Of course in a bigger system with a factory, the pluggable app might handle creating the context, e.g. by looking at the incoming URL.

## Per-Request Context

Another benefit: different flavors of component based on the "context".
The app can render using a container that has a context value.
The plugin can then provide a component for the default and a different implementation for a certain context.

We now have two kinds of context:

```{literalinclude} ../examples/pluggable/custom_context/site/contexts.py
---
start-after: from dataclasses
---
```

The site then makes a local flavor of the `Greeter` component, for use with the new kind of context:

```{literalinclude} ../examples/pluggable/custom_context/site/components.py
---
start-after: from wired_injector
---
```

The template in the view doesn't have to change.
Any other components that use a `Greeting` component, don't have to change.
They just get a `FrenchGreeting` in appropriate cases.
