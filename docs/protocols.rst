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
- app ships a navbar with a logo with a passed arg
- a test constructs an instance, tests a vdom
- mypy says all is good

plugin_navbar
- a plugin wants to provide a replacement
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
