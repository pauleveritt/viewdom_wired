from .site import main, expected


def test():
    actual = main()
    return expected, actual
