project = 'viewdom_wired'
copyright = '2020, Paul Everitt <pauleveritt@me.com>'
author = 'Paul Everitt <pauleveritt@me.com>'
release = '0.0.1'
extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
]
templates_path = ['_templates']
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = 'viewdom'
html_theme_options = dict(
    extra_footer='Theme by the <a href="https://ebp.jupyterbook.org">'
                 + 'Executable Book Project</a>.',
    repository_url='https://github.com/pauleveritt/viewdom_wired',
    use_repository_button=True,
)
html_css_files = [
    'custom.css',
]
html_sidebars = {
    "**": [
        'subtitle.html',
        'sidebar-search-bs.html',
        'sbt-sidebar-nav.html',
    ]
}
myst_admonition_enable = True
