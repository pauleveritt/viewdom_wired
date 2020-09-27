from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
changes = readfile('CHANGES.rst')

requires = [
    'viewdom',
    'wired',
    'wired_injector',
    'venusian',
]

docs_require = [
    'Sphinx',
]

tests_require = [
    'pytest',
    'mypy',
    'pytest-mypy',
    'ipython',
]

setup(
    name='viewdom_wired',
    description=(
        'Injectable and plugabble components and services for viewdom'
    ),
    version='0.1.0',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://viewdom_wired.readthedocs.io',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={"viewdom_wired": ["py.typed"]},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=requires,
    extras_require={'docs': docs_require, 'tests': tests_require},
    zip_safe=False,
    keywords=','.join(
        [
            'web',
            'html',
            'components',
            'templates',
        ]
    ),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
