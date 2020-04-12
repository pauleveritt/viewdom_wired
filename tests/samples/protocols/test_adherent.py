from viewdom.h import H


def test_adherent_altlogo():
    from samples.protocols.adherent.app import Logo
    from samples.protocols.adherent.plugins.logo import NoAltLogo
    logo: Logo = NoAltLogo(src='alt.png')
    vdom = logo()
    assert vdom == H(tag='img', props={'src': 'alt.png'}, children=[])


def test_adherent_render():
    from samples.protocols.adherent.site import main
    assert main() == '<nav><img src="logo.png"/></nav>'
