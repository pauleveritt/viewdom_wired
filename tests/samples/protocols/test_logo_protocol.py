# from viewdom import VDOM
#
#
# def test_logo_protocol_altlogo():
#     from viewdom_wired.samples.protocols.logo_protocol.plugins.logo import NoAltLogo
#     logo = NoAltLogo(src='alt.png')
#     vdom = logo()
#     assert vdom == VDOM(
#         tag='img',
#         props=dict(alt='No alt Needed', src='alt.png'),
#         children=[]
#     )
#
#
# def test_logo_protocol_render():
#     from viewdom_wired.samples.protocols.logo_protocol.site import main
#     assert main() == '<nav><img alt="No alt Needed" src="logo.png"/></nav>'
