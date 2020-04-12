"""
Views for the site.

Would likely be Flask views or Sphinx context handlers.
"""

from viewdom import html

from ..plugins.greeting import Greeting  # noqa


def greeting_view():
    template = '<{Greeting}/>'
    return html(template)
