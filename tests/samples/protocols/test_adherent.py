# from viewdom import VDOM
#
#
# def test_adherent_altlogo():
#     from viewdom_wired.samples.protocols.adherent.plugins.logo import NoAltLogo
#     logo = NoAltLogo(src='alt.png')
#     vdom = logo()
#     assert vdom == VDOM(
#         tag='img',
#         props=dict(src='alt.png', title='No Alt Logo'),
#         children=[]
#     )
#
#
# def test_adherent_render():
#     from viewdom_wired.samples.protocols.adherent.site import main
#     assert main() == '<nav><img src="logo.png" title="No Alt Logo"/></nav>'
