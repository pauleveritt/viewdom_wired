from viewdom import html

from ..app import Navbar

LOGO_ALT = 'Site Logo'
LOGO_SRC = 'logo.png'


def greeting_view():
    return html('''
    <{Navbar} logo_alt={LOGO_ALT} logo_src={LOGO_SRC} />''')
