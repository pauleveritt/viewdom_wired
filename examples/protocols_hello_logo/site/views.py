from viewdom import html

from ..app import Navbar

LOGO_SRC = 'logo.png'


def greeting_view():
    return html('''
    <{Navbar} logo_src={LOGO_SRC} />
    ''')
