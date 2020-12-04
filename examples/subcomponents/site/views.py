"""
Views for the site.

Would likely be Flask views or Sphinx context handlers.
"""

from viewdom import html

from ..plugins.greeting import Greeting


def greeting_view():
    return html(
        '''
    <{Greeting}/>
    '''
    )
