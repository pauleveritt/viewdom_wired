======
Blocks
======

Jinja2 has a concept of blocks, where child templates can point to a parent template and "fill in the blanks".
This matches a pattern in React components, where you can pass in components as props, even "render props" as callables.

However, React components do *not* have an important feature of Jinja2 blocks: the ability for the parent to have default values which the child can grab via ``super()``.
Let's see how that could be implemented in ``viewdom_wired``.

