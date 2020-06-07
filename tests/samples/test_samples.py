def test_samples_hello_world():
    from samples.hello_world import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_hello_app():
    from samples.hello_app import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_app_plugin_site():
    from samples.app_plugin_site.site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_app_decorators_render():
    from samples.app_decorators_render.site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_subcomponents_render():
    from samples.subcomponents.site import main
    assert main() == '<h1>Hello viewdom_wired<span>!</span></h1>'


def test_samples_override():
    from samples.override.site import main
    assert main() == '<h1>Hello My Site</h1>'


def test_samples_context():
    from samples.context.site import main
    assert main() == '<h1>Hello Mary</h1>'


def test_samples_site_context():
    from samples.custom_context.site import main
    results = main()
    regular_result = results['regular_result']
    assert regular_result == '<h1>Hello Mary</h1>'
    french_result = results['french_result']
    assert french_result == '<h1>Bonjour Marie</h1>'
