from dataclasses import dataclass

from viewdom import html, VDOM


@dataclass
class Super:
    parent_children: VDOM = ()

    def __call__(self) -> VDOM:
        return self.parent_children


@dataclass
class Layout:
    """ A layout that governs all the site """
    navitems: VDOM = html('<span>Default Choice</span>')
    children: VDOM = ()

    def __call__(self) -> VDOM:
        return html('''\n
            <nav>
                {self.navitems}
            </nav>
            {self.children}
        ''')


@dataclass
class Page:
    """ A single page """

    @property
    def navitems(self):
        return html('<{Super} name="navitems"/><span>Extra Choice</span>')

    def __call__(self) -> VDOM:
        return html('''\n
        <{Layout} navitems={self.navitems}>
        <main>The Page</main>
        <//>
        ''')
