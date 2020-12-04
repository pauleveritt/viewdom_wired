"""
Views for the site.

Would likely be Flask views or Sphinx context handlers.
"""

from viewdom import html, VDOM

from ..plugins.greeting import Greeting


def greeting_view() -> VDOM:
    return html('<{Greeting}/>')
