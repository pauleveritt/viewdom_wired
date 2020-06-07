from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected

from samples.subcomponents.app import PunctuationCharacter
from viewdom_wired import component


@component()
@dataclass
class Punctuation:
    character: str = injected(PunctuationCharacter, attr='symbol')

    def __call__(self):
        return html('<span>{self.character}</span>')
