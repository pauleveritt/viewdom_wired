from dataclasses import dataclass

from viewdom import html, VDOM
from wired_injector import injectable
from wired_injector.pipeline.operators import Get

from viewdom_wired import component

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated  # type: ignore # noqa: F401


@injectable()
@dataclass
class Settings:
    first_name: str = 'Settings'


@component()
@dataclass
class Greeting:
    first_name: Annotated[str, Get(Settings, attr='first_name')]

    def __call__(self) -> VDOM:
        return html('<h1>Hello {self.first_name}</h1>')
