from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable
from wired_injector.operators import Attr, Context

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@injectable()
@dataclass
class Greeting:
    name: Annotated[str, Context(), Attr('name')]

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
