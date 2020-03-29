def test_samples_hello_world():
    from samples.hello_world import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_hello_app():
    from samples.hello_app import main
    assert main() == '<h1>Hello viewdom_wired</h1>'


def test_samples_app_plugin_site():
    from samples.app_plugin_site import main
    assert main() == '<h1>Hello viewdom_wired</h1>'
