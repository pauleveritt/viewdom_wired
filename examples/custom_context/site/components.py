from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable
from wired_injector.operators import Attr, Context

from .contexts import FrenchCustomer
from ..plugins.greeting import Greeting

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


# Customizability:
# This replaces lookups for Greeting, but only
# when the context is a FrenchCustomer


@injectable(for_=Greeting, context=FrenchCustomer)
@dataclass
class FrenchGreeting:
    name: Annotated[str, Context(), Attr('name')]

    def __call__(self):
        return html('<h1>Bonjour {self.name}</h1>')
