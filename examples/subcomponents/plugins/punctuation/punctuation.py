from dataclasses import dataclass

from viewdom import html
from wired_injector import injectable
from wired_injector.operators import Attr, Get

from examples.subcomponents.app import PunctuationCharacter

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@injectable()
@dataclass
class Punctuation:
    character: Annotated[
        str,
        Get(PunctuationCharacter),
        Attr('symbol'),
    ]

    def __call__(self):
        return html('<span>{self.character}</span>')