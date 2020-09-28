def test_samples_hello_world():
    from examples.hello_world.app import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_hello_children():
    from examples.hello_children.app import main
    assert '<h1>Hello viewdom_wired</h1><span>Children</span>' == main()


def test_samples_hello_app():
    from examples.hello_app.site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_app_plugin_site():
    from examples.app_plugin_site.site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_app_decorators_render():
    from examples.app_decorators_render.site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_subcomponents_render():
    from examples.subcomponents.site import main
    assert main() == '<h1>Hello viewdom_wired<span>!</span></h1>'


def test_samples_override():
    from examples.override.site import main
    assert main() == '<h1>Hello My Site</h1>'


def test_samples_context():
    from examples.context.site import main
    assert main() == '<h1>Hello Mary</h1>'


def test_samples_custom_context():
    from examples.custom_context.site import main
    results = main()
    regular_result = results['regular_result']
    assert regular_result == '<h1>Hello Mary</h1>'
    french_result = results['french_result']
    assert french_result == '<h1>Bonjour Marie</h1>'


def test_samples_protocols_hello_logo():
    from examples.protocols_hello_logo.site import main
    assert main() == '<nav><img src="logo.png"/></nav>'


def test_samples_logo_protocol():
    from examples.logo_protocol.site import main
    assert main() == '<nav><img alt="No alt Needed" src="logo.png"/></nav>'


def test_samples_adherent():
    from examples.adherent.site import main
    assert '<nav><img src="logo.png" title="No alt Needed"/></nav>' == main()
