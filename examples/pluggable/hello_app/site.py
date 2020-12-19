from dataclasses import dataclass

from viewdom import html, VDOM

from viewdom_wired import component
from .plugins import greeting
from .plugins.greeting import Greeting

plugins = (greeting,)


@component(for_=Greeting)
@dataclass
class SiteGreeting:
    name: str = 'Site'

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.name}</h1>')
