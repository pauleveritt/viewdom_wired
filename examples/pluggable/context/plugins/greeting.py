from dataclasses import dataclass

from viewdom import html
from wired_injector.pipeline.operators import Attr, Context

from viewdom_wired import component

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore # noqa: F401


@component()
@dataclass
class Greeting:
    name: Annotated[str, Context(), Attr('name')]

    def __call__(self):
        return html('<h1>Hello {self.name}</h1>')
