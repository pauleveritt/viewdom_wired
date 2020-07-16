"""
A simple site which uses (a) a pluggable app and (b) a plugin with some
known components.
"""

from viewdom import html

from viewdom_wired import render
from .app import make_app
from .plugin import Block, Layout, Page


def main() -> str:
    registry = make_app((Block, Layout, Page))
    container = registry.create_container()
    return render(html('<{Page}/>'), container)
