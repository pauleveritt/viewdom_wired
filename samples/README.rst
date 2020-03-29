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

- Richer app class with a scanner, switch to decorators for components
