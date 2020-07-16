from dataclasses import dataclass

from viewdom import html, VDOM


@dataclass
class Layout:
    """ A layout that governs all the site """
    navitems: VDOM = html('<span>Layout1</span>')

    def __call__(self) -> VDOM:
        return html('''\n
        <body>
            <nav>
                {self.navitems}
            </nav>
        </body>
        ''')


@dataclass
class Page:
    """ A single page """
    navitems: VDOM = html('<span>Page1</span>')

    def __call__(self) -> VDOM:
        return html('''\n
        <{Layout} navitems={self.navitems}>
        <//>
        ''')
