"""
Replace the greeter plugin's Greeter with a different Greeter.
"""

from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable

from ..plugins.greeting import Greeting


@injectable(for_=Greeting)
@dataclass
class SiteGreeting:
    name: str = 'My Site'

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
