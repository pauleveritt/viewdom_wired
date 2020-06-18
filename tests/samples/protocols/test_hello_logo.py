from viewdom import VDOM


def test_hello_logo_altlogo():
    from samples.protocols.hello_logo.app import Logo
    from samples.protocols.hello_logo.plugins.logo import NoAltLogo
    logo: Logo = NoAltLogo(src='alt.png')
    vdom = logo()
    assert vdom == VDOM(tag='img', props={'src': 'alt.png'}, children=[])


def test_hello_logo_render():
    from samples.protocols.hello_logo.site import main
    assert main() == '<nav><img src="logo.png"/></nav>'
