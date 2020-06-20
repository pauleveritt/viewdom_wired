from dataclasses import dataclass

from viewdom import html

from viewdom_wired import component


@component()
@dataclass
class Greeting:
    name: str = 'viewdom_wired'

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
