from viewdom_wired.render import render, component, register_component

__version__ = '0.1.0'


def hello():
    return 1


__all__ = [
    'component',
    'register_component',
    'render',
]
