from .app import main, expected


def test():
    actual = main()
    return expected, actual
