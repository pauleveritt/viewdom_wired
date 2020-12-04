"""

Pluggable app class with a registry and decorator scanner.

"""

from .site import main, expected


def test():
    actual = main()
    return expected, actual
