from viewdom import VDOM

def test_logo_protocol_altlogo():
    from samples.protocols.logo_protocol.app import Logo
    from samples.protocols.logo_protocol.plugins.logo import NoAltLogo
    logo: Logo = NoAltLogo(src='alt.png')
    vdom = logo()
    assert vdom == VDOM(tag='img', props={'src': 'alt.png'}, children=[])


def test_logo_protocol_render():
    from samples.protocols.logo_protocol.site import main
    assert main() == '<nav><img src="logo.png"/></nav>'
