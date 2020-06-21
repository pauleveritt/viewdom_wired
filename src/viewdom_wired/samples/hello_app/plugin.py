from dataclasses import dataclass

from viewdom import html, VDOM


@dataclass
class Greeting:
    """ A simple component with one argument """
    name: str = 'viewdom_wired'

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>')
