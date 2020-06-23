==================
Usage With Classes
==================

Let's write a basic application using the pluggability ideas in ``viewdom_wired``.
We'll start with something very basic and gradually introduce some of the basic ideas.
All of these examples are in the repository's ``examples`` directory with tests that cover them in the ``tests`` directory.

hello_world
===========

The simplest possible example:
A single function which recreates the universe whenever it is run:

.. literalinclude:: ../examples/hello_world/app.py


hello_app
=========

Of course that's not very real-world.
Let's show a case that splits the three roles.

First, a pluggable app:

.. literalinclude:: ../examples/hello_app/app.py

Then, a third-party plugin for the app, providing a component that can be used in a site:

.. literalinclude:: ../examples/hello_app/components.py

Finally, the site itself, which uses the app and the third-party plugin to render a response:

.. literalinclude:: ../examples/hello_app/site.py

app_plugin_site
===============

Let's re-organize the layout to emphasize the 3 roles: app, plugins, and a site.

The app, which stores the registry:

.. literalinclude:: ../examples/app_plugin_site/site/__init__.py

A ``greeting`` plugin with a ``wired_setup`` function to set itself up:

.. literalinclude:: ../examples/app_plugin_site/plugins/greeting/__init__.py

The plugin's component doesn't change much:

.. literalinclude:: ../examples/app_plugin_site/plugins/greeting/component.py

And finally a site that uses the pluggable app and the plugin:

.. literalinclude:: ../examples/app_plugin_site/site/__init__.py

The site now has a "view" that can render a request.

.. literalinclude:: ../examples/app_plugin_site/site/views.py


app_decorators_render
=====================

We now switch to an app which can register decorator-based plugins, passing them the registry for self-configuration.

The pluggable app is richer, including a ``venusian`` decorator scanner.
You can now tell the app to setup a plugin module:

.. literalinclude:: ../examples/app_decorators_render/site/__init__.py

The plugin's ``wired_setup`` can now register itself, getting passed the app instance:

.. literalinclude:: ../examples/app_decorators_render/plugins/greeting/__init__.py

The plugin has a component:

.. literalinclude:: ../examples/app_decorators_render/plugins/greeting/greeting.py

We again have a site:

.. literalinclude:: ../examples/app_decorators_render/site/__init__.py

But this time, the site has a "view" which handles the response.
It uses the plugin's ``Greeting`` component:

.. literalinclude:: ../examples/app_decorators_render/site/views.py

override
========

Now we get into the strength of ``viewdom_wired``: a registration which *replaces* component from another package.

Nothing changes in the pluggable app nor in the plugins.
The site is in control: it can register replacements.

Here is the site, which now scans for local components which might add to *or replace* components:

.. literalinclude:: ../examples/override/site/__init__.py

The site now has a components file:

.. literalinclude:: ../examples/override/site/components.py

The site's ``views.py`` remains the same.
When its template asks for a ``Greeting`` component, a different implementation is provided.

.. literalinclude:: ../examples/override/site/views.py

One thing that is nice about this: we didn't use subclassing to establish the is-a relationship between ``Greeting`` and ``SiteGreeting``.
Instead, the registration handled this with the ``for_``.

context
=======

Components don't have to get all their info from passed-in props.
They can ask the injector to get information for them, for example, from the ``wired`` container's context.

The app changes, as ``render`` now accepts a context, which it puts in the container:

.. literalinclude:: ../examples/context/app/__init__.py

Here's a **big** point: the component asks the *injector* to get the *context*.
Thus, the parent components don't have to pass this all the way down.
Moreover, the injector is asked to get a specific attribute off the context, which is nice for two reasons:

- The consumer of this component could pass in a different value, superseding the injector value

- The component has a smaller surface area with the outside world, instead of getting the entire context

.. literalinclude:: ../examples/context/plugins/greeting/greeting.py

The site defines different kinds of contexts:

.. literalinclude:: ../examples/context/site/contexts.py

The site then makes a context to use during rendering:

.. literalinclude:: ../examples/context/site/__init__.py

Of course in a bigger system, the pluggable app might handle creating the context, e.g. by looking at the incoming URL.

custom_context
==============

Another benefit: different flavors of component based on the "context".
The app can render using a container that has a context value.
The plugin can then provide a component for the default and a different implementation for a certain context.

We now have two kinds of context:

.. literalinclude:: ../examples/custom_context/site/contexts.py

The site then makes a local flavor of the ``Greeter`` component, for use with the new kind of context:

.. literalinclude:: ../examples/custom_context/site/components.py

The template in the view doesn't have to change.
Any other components that use a ``Greeting`` component, don't have to change.
They just get a ``FrenchGreeting`` in appropriate cases.

Protocols: hello_logo
=====================

In ``overrides`` we saw an example of a ``Greeting`` component, from a plugin, which was *replaced* with site-specific ``Greeting``.
Then in ``custom_context`` we saw a very useful variation of that: use ``Greeting`` most of the time, but replace it with ``FrenchGreeting`` for a certain context.
The caller didn't know that ``FrenchGreeting`` even existed...it asked for a ``Greeting`` but got a different implementation.

There are two flaws, though:

- The definition of a ``Greeting`` is an *implementation*. It sure would be nice if ``Greeting`` was abstract, all implementations equal, and any one implementation could be removed.

- There's no *contract*. How do you know if you made a kind of ``Greeter``?

In these next examples we switch to using `PEP 544 Protocols <https://www.python.org/dev/peps/pep-0544/>`_.
With these, when a template asks for a ``Greeter``, it is referring to an abstract "Greeter".
Each implementation in the registry says "I'm a kind of ``Greeter``."
Even better, ``mypy`` can do some (rudimentary) confirmation of the contract.

We will start with a good example of the problem being solved, before adding PEP 544 protocols:

- A site is using a pluggable app which has a default navbar that contains a logo

- The site *also* installs a plugin which customizes the logo with one that has no ``alt``

We start with the pluggable app.
It has two components:

.. literalinclude:: ../examples/protocols_hello_logo/site/components.py

The ``logo`` plugin, though, replaces once of those components:

.. literalinclude:: ../examples/custom_context/plugins/logo/components.py

When the site's view renders, it gets a navbar containing an image, but with no logo:

.. code-block:: html

  <nav><img src="logo.png"/></nav>

logo_protocol
=============

This example has a fundamental change.
The pluggable app still has ``Navbar`` and ``Logo``, but they are *protocols*.
They aren't actual components, just the abstract definition of the contract:

.. literalinclude:: ../examples/logo_protocol/app/protocols.py

That looks pretty cool: anybody that wants to make a different kind of "Logo" will now know exactly what's required.
From a component perspective, the fields roughly conform to the "props" that need to be passed in when a template uses a component.
It's also a way for static typing tools (IDEs, ``mypy``) to help tell you when contracts are broken.

Each protocol subclasses from two bases.
``Component`` is a protocol with exactly one contract: a component must have a ``__call__`` that returns a ``VDOM``.
``Protocol`` is the flag that says this class-looking-thingy is a PEP 544 protocol.

The pluggable app then ships with component implementations of each protocol:

.. literalinclude:: ../examples/logo_protocol/app/components.py

Like we saw earlier, the ``@component`` decorator says it is ``for_=Logo``.
But this time, ``Logo`` isn't a component implementation.
Instead, we are saying the following is an implementation of the abstract idea of a ``Logo``.

The plugin then overrides just the logo:

.. literalinclude:: ../examples/logo_protocol/plugins/logo/components.py

Finally, in the site's view, we use ``Navbar`` in a template:

.. literalinclude:: ../examples/logo_protocol/site/views.py

But the ``Navbar`` that we import is the *protocol* not a particular implementation.

In this site, the only ``Navbar`` implementation is in the pluggable app's ``DefaultNavbar``, shown above.
It has a template asking for a ``Logo``, which is the *protocol* for a logo.
Since the site loaded the plugin, and the plugin overrode the ``DefaultLogo`` with ``NoAltLogo``, the latter is used.

Alas, we don't yet get ``mypy`` to tell us if we break the contract.
We'll add that next.

adherent
========

The ``component`` decorator tells our registry that we have a ``Navbar``.
But that's a runtime idea, outside of Python and ``mypy`` and static type checking.
We need a way to tell the type checker that we have some that adheres to a particular protocol, and thus yell at me if I break the contract.

Here is an ``@adherent`` decorator which does so:

.. literalinclude:: ../examples/adherent/app/decorator.py

The pluggable app's default implementations now additionally say that they "adhere" to this protocol:

.. literalinclude:: ../examples/adherent/app/components.py

For now it is an extra decorator, used for systems that embrace PEP 544 protocols.

This implementation runs correctly: ``DefaultNavbar`` passes in ``alt`` but the ``NoAltLogo`` component doesn't actually ask for it.
However, static typing -- ``mypy`` -- knows you broke the contract:

.. code-block:: bash

  plugins/logo/components.py:11: error: Argument 1 has incompatible type "Type[NoAltLogo]"; expected "Type[Logo]"
  Found 1 error in 1 file (checked 1 source file)

.. note::

  If this works out, I'll convert ``viewdom_wired`` to be protocol-based, eliminate the extra decorator, and fold this functionality into ``@component``.

.. note::

  PEP 544 claims that you can use "subclassing" to assert a class adheres to a protocol.
  However ``mypy`` doesn't support it (and in fact, gets kind of mad about it.)
  It's a reported issue.
