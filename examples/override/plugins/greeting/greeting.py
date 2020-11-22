from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable


@injectable()
@dataclass
class Greeting:
    name: str = 'viewdom_wired'

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
