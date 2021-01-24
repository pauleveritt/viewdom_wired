from dataclasses import dataclass

from viewdom import html
from wired_injector.pipeline.operators import Attr, Context

from viewdom_wired import component
from .contexts import FrenchCustomer
from ..plugins.greeting import Greeting

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore # noqa: F401


# Customizability:
# This replaces lookups for Greeting, but only
# when the context is a FrenchCustomer


@component(for_=Greeting, context=FrenchCustomer)
@dataclass
class FrenchGreeting:
    name: Annotated[str, Context(), Attr('name')]

    def __call__(self):
        return html('<h1>Bonjour {self.name}</h1>')
