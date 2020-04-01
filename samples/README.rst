===================
Sample Applications
===================

These examples gradually build from simplest possible hello world into a larger application with plugins and sites that use the app and plugins.


``hello_world``
===============

The simplest possible example.
A single function which recreates the universe whenever it is run:

- Make a registry
- Register a component
- Make a container
- Render the component

``hello_app``
=============

Put the app part in its own file and the component in its own file.


``app_plugin_site``
===================

Re-organize the directory to mimic a site which installs an app package and a plugin.
Registry gets passed to the plugins.


``app_decorators_render``
=========================

Richer app class with a scanner and a render method.
Switch to supporting decorators for components.

``override``
============

The site replaces ``Greeting`` with its own implementation.

``context``
===========

The app can render using a container that has a context value.
The plugin can then provide a component for the default and a different implementation for a certain context.


``custom_context``
==================

The site adds a ``Greeter`` component to be used only for a certain ``Customer`` context.


- Rendering with a context
- Multiple plugins
- Multiple plugins with the same component
- Override plugin with site-specific component
