"""

Views for the site.

Would likely be Flask views or Sphinx context handlers.

"""

from viewdom import html

# noinspection PyUnresolvedReferences
from ..plugins.greeting import Greeting


def greeting_view():
    template = '<{Greeting}/>'
    return html(template)
