from dataclasses import dataclass

from viewdom import html
from viewdom_wired import component
from wired_injector.operators import Attr, Get

from ..app.factories import PunctuationCharacter

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore


@component()
@dataclass
class Punctuation:
    character: Annotated[
        str,
        Get(PunctuationCharacter),
        Attr('symbol'),
    ]

    def __call__(self):
        return html('<span>{self.character}</span>')
