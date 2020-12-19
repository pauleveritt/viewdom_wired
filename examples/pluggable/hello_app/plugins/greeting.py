from dataclasses import dataclass

from viewdom import html, VDOM

from viewdom_wired import component


@component()
@dataclass
class Greeting:
    name: str = 'Plugin'

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>')
