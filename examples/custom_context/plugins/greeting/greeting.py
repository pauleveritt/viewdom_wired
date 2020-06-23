from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected, Context

from viewdom_wired import component


@component()
@dataclass
class Greeting:
    name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
