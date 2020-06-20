from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected, Context

from viewdom_wired import component
from .contexts import FrenchCustomer
from ..plugins.greeting import Greeting

# Customizability:
# This replaces lookups for Greeting, but only
# when the context is a FrenchCustomer
@component(for_=Greeting, context=FrenchCustomer)
@dataclass
class FrenchGreeting:
    name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<h1>Bonjour {self.name}</h1>')
