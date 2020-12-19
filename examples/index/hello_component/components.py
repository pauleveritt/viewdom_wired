from dataclasses import dataclass

from viewdom import html, VDOM

from viewdom_wired import component


@component()
@dataclass
class Greeting:
    first_name: str

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.first_name}</h1>')
