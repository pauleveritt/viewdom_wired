project = 'viewdom_wired'
html_title = 'viewdom_wired'
copyright = '2020, Paul Everitt <pauleveritt@me.com>'
author = 'Paul Everitt <pauleveritt@me.com>'
release = '0.1.0'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'myst_parser',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
]
templates_path = ['_templates']
html_theme = 'sphinx_book_theme'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']
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
myst_enable_extensions = [
    'colon_fence',
]
myst_url_schemes=['http', 'https', 'mailto']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.7', None),
    'wired': ('https://wired.readthedocs.io/en/stable', None),
    'viewdom': ('https://viewdom.readthedocs.io/en/latest', None),
}
