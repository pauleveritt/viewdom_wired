from dataclasses import dataclass

from viewdom import html


@dataclass
class Greeting:
    name: str = 'viewdom_wired'

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
