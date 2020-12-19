from dataclasses import dataclass

from wired_injector import injectable


@injectable()
@dataclass
class PunctuationCharacter:
    """ A configurable symbol to use in punctuation """

    symbol: str = '!'
