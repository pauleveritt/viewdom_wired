==================
Usage With Classes
==================

Let's write a basic application using the pluggability ideas in ``viewdom_wired``.
We'll start with something very basic and gradually introduce some of the basic ideas.
All of these examples are in the repository's ``samples`` directory with tests that cover them in the ``tests`` directory.

hello_world
===========

The simplest possible example:
A single function which recreates the universe whenever it is run:

.. literalinclude:: ../samples/hello_world/app.py


hello_app
=========

Of course that's not very real-world.
Let's show a case that splits the three roles.

First, a pluggable app:

.. literalinclude:: ../samples/hello_app/app.py

Then, a third-party plugin for the app, providing a component that can be used in a site:

.. literalinclude:: ../samples/hello_app/components.py

Finally, the site itself, which uses the app and the third-party plugin to render a response:

.. literalinclude:: ../samples/hello_app/site.py

app_plugin_site
===============

Let's re-organize the layout to emphasize the 3 roles: app, plugins, and a site.

The app, which stores the registry:

.. literalinclude:: ../samples/app_plugin_site/site/__init__.py

A ``greeting`` plugin with a function to set itself up:

.. literalinclude:: ../samples/app_plugin_site/plugins/greeting/__init__.py

And finally a site that uses the two.
In this case, the *site* does the plugin setup -- we will move that in the next step to the app:

.. literalinclude:: ../samples/app_plugin_site/site/__init__.py

app_decorators_render
=====================

We now switch to an app which can register plugins, passing them the registry for self-configuration.

The pluggable app is richer, including a ``venusian`` decorator scanner:

.. literalinclude:: ../samples/app_decorators_render/site/__init__.py

The plugin has an entry point to register itself, getting passed the app instance:

.. literalinclude:: ../samples/app_decorators_render/plugins/greeting/__init__.py

The plugin has a component:

.. literalinclude:: ../samples/app_decorators_render/plugins/greeting/greeting.py

We again have a site:

.. literalinclude:: ../samples/app_decorators_render/site/__init__.py

But this time, the site has a "view" which handles the response:

.. literalinclude:: ../samples/app_decorators_render/site/views.py

override
========

Now we get into the strength of ``viewdom_wired``: a registration which replaces a component from another package.

Nothing changes in the pluggable app nor in the plugins.
The site is in control: it can register replacements.

Here is the site, which now scans for local components which might add to *or replace* components:

.. literalinclude:: ../samples/override/site/__init__.py

The site now has a components file:

.. literalinclude:: ../samples/override/site/components.py

The site's ``views.py`` remains the same.
When its template asks for a ``Greeting`` component, a different implementation is provided.

.. literalinclude:: ../samples/override/site/views.py

One thing that is nice about this: we didn't use subclassing to establish the is-a relationship between ``Greeting`` and ``SiteGreeting``.
Instead, the registration handled this with the ``for_``.

context
=======

Components don't have to get all their info from passed-in props.
They can ask the injector to get information for them, for example, from the ``wired`` container's context.

The app changes, as ``render`` now accepts a context, which it puts in the container:

.. literalinclude:: ../samples/context/app/__init__.py

Here's a **big** point: the component asks the *injector* to get the *context*.
Thus, the parent components don't have to pass this all the way down.
Moreover, the injector is asked to get a specific attribute off the context, which is nice for two reasons:

- The consumer of this component could pass in a different value, superseding the injector value

- The component has a smaller surface area with the outside world, instead of getting the entire context

.. literalinclude:: ../samples/context/plugins/greeting/greeting.py

The site defines different kinds of contexts:

.. literalinclude:: ../samples/context/site/contexts.py

The site then makes a context to use during rendering:

.. literalinclude:: ../samples/context/site/__init__.py

Of course in a bigger system, the pluggable app might handle creating the context, e.g. by looking at the incoming URL.

custom_context
==============

Another benefit: different flavors of component based on the "context".
The app can render using a container that has a context value.
The plugin can then provide a component for the default and a different implementation for a certain context.

We now have two kinds of context:

.. literalinclude:: ../samples/custom_context/site/contexts.py

The site then makes a local flavor of the ``Greeter`` component, for use with the new kind of context:

.. literalinclude:: ../samples/custom_context/site/components.py

The template in the view doesn't have to change.
Any other components that use a ``Greeting`` component, don't have to change.
They just get a ``FrenchGreeting`` in appropriate cases.