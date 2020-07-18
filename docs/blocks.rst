======
Blocks
======

Jinja2 has a concept of blocks, where child templates can point to a parent template and "fill in the blanks".
This matches a pattern in React components, where you can pass in components as props, even "render props" as callables.

However, React components do *not* have an important feature of Jinja2 blocks: the ability for the parent to have default values which the child can grab via ``super()``.
Let's see how that could be implemented in ``viewdom_wired``.

Jinja2
======

In Jinja2 one would do something like this.
First, a ``layout.html`` file that defined a block, along with some default content:

.. code-block:: html

    <body>
        <nav>
            {% block navitems %}
                <span>Default Nav</span>
            {% endblock %}
        </nav>
    </body>

Then, some other "child" template would say (a) I want to use layout and (b) I am filling that block. (Note that (b) is optional.)

.. code-block:: html

    {% extends "layout.html" %}
    {% block navitems %}
        {{ super() }}
        <span>Extra Nav</span>
    {% endblock %}

Jinja2 has some scoping rules for blocks which might be hard to follow, but most usage is simple and follows the above static content.

JSX
===

In JSX the pattern for layouts
- Nesting
- TSX and typing
- Drawback...no concept of "super()"

