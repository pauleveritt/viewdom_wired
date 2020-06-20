from viewdom import html

from ..app import Navbar  # noqa

LOGO_SRC = 'logo.png'


def greeting_view():
    template = '<{Navbar} logo_src={LOGO_SRC} />'
    return html(template)
