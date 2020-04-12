====================
Usage With Protocols
====================

In :doc:`./usage` we saw how to provide different flavors of components, using ``for_`` to establish the relationship.
This solves the registration problem, but other parts of your code don't know that ``SiteGreeter`` is a kind of ``Greeter``.

While we could use subclassing, sharing the implementation has downsides.
Python's `PEP 544 <https://www.python.org/dev/peps/pep-0544/>`_ uses "protocols" and *structural* subtyping.
With this, different implementations of ``Greeting`` can adhere to a contract, and tools such as ``mypy`` can enforce it.
Fortunately, ``wired`` can use protocols in the ``for_`` to register implementations.

Let's write an application showing the use of protocols in a component system.

hello_logo
==========

We have a pluggable app that ships with its own components: a ``Navbar`` which has a ``Logo`` subcomponent.
The app changes slightly to scan the ``components.py`` module for registrations:

.. literalinclude:: ../samples/protocols/hello_logo/app/app.py

The two built-in components:

.. literalinclude:: ../samples/protocols/hello_logo/app/components.py

The site is using a plugin which replaces the built-in logo with one that allows an ``alt`` value:

.. literalinclude:: ../samples/protocols/hello_logo/plugins/logo/components.py

The site has a view with a template which renders a ``Navbar``:

.. literalinclude:: ../samples/protocols/hello_logo/site/views.py

The result is ``'<nav><img src="logo.png" alt="Logo"/></nav>'``.

If you look at the test, you can see how we constructed an instance, but used a type hint to say this was a "Logo":

.. literalinclude:: ../tests/samples/protocols/test_hello_logo.py
    :emphasize-lines: 7

Sure, the tests pass.
But ``NoAltLogo`` isn't a kind of ``Logo``.
Someone else might use it, try to pass in an ``alt``, and fail.

We could solve this with subclassing.
But as PEP 544 points out, the world of Python has learned the hazards of sharing implementation.
Is there some other way to say ``NoAltLogo`` is a kind of ``Logo`` and have Python static typing tell us when contracts are broken?

Protocols
=========

First, let's break the concept from the implementation: ``Logo`` will be a PEP 544 protocol.

The pluggable app will define the ``Logo`` protocol then provide a ``DefaultLogo`` implementation of that protocol:

.. literalinclude:: ../samples/protocols/logo_protocol/plugins/logo/components.py

The ``NoAltLogo`` component in the plugin doesn't need to change.
But when it says it is ``for_=Logo``, it's "for" a protocol, not a particular implementation of that protocol.

This all works well, because ``wired`` just treats ``Logo`` as a marker, whether a class or a "protocol".

However, we still don't have a way to say ``NoAltLogo`` is a ``Logo``, much less enforce it with ``mypy``.

adherent
========

In the ``mypy`` tracker, Glyph `pointed to a decorator <https://github.com/python/mypy/issues/4717#issuecomment-454609539>`_ which could say "the following class implements a certain protocol."
Let's use it.



If you later make an instance of that class, but with a type hint saying the protocol name,


plugin_navbar
- a plugin wants to provide a replacement
    - Gets src from config, so it doesn't have to be passed down
    - Provides alt support
- the replacement doesn't quite follow the convention
- a test constructs an instance with a vdom which passes
- why didn't this get caught by mypy?

logo_protocol
- have Logo as a protocol with a built-in logo that adheres
- test passes, mypy passes
- but the replacement fails, it doesn't adhere to the protocol

Futures
- IDEs could red-squiggly when the contract was violated
- mypy and IDEs could understand the template string and validate/autocomplete based on protocol
