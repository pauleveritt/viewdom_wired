from viewdom import html

from ..app import Navbar  # noqa

LOGO_ALT = 'Site Logo'
LOGO_SRC = 'logo.png'


def greeting_view():
    template = '<{Navbar} logo_alt={LOGO_ALT} logo_src={LOGO_SRC} />'
    return html(template)
