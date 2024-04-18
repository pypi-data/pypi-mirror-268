import pathlib
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='turandot',
    version='3.1.4',
    description='Turandot Markdown Converter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    author='Martin Obrist',
    author_email='dev@obrist.email',
    url='https://turandot.readthedocs.io',
    project_urls={
        'Documentation': 'https://turandot.readthedocs.io',
        'Source Code': 'https://gitlab.com/dinuthehuman/turandot',
        'Issue Tracker': 'https://gitlab.com/dinuthehuman/turandot/-/issues'
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Text Processing :: Markup :: Markdown',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='markdown, citeproc',
    packages=find_packages(where='.', exclude=['tests', 'tasks']),
    python_requires='>=3.10, <4',
    include_package_data=True,
    setup_requires=['wheel'],
    install_requires=[
        "beautifulsoup4==4.11.2",
        "colour==0.1.5",
        "jinja2==3.1.3",
        "lxml==5.1.0",
        "Mako==1.2.4",
        "markdown==3.5.2",
        "markdown-captions==2.1.2",
        "markdown-katex==202112.1034",
        "md_citeproc==0.2.2",
        "Pygments==2.17.2",
        "python-frontmatter==1.0.0",
        "pyyaml==6.0.1",
        "requests==2.31.0",
        "ruamel.yaml==0.18.6",
        "sqlalchemy==2.0.27",
        "urllib3==2.2.1",
        "weasyprint==56.0",
    ],
    extras_require={
        'tk': [
            "tkhtmlview",
            "bidict"
        ],
        'gtk': [
            "pygobject==3.46.0"
        ],
        'dev': [
            "gitpython==3.1.42",
            "mkdocs==1.5.3",
            "mkdocstrings==0.24.1",
            "twine==5.0.0",
            "pytest==8.0.2",
            "nose==1.3.7",
            "invoke==2.2.0"
        ],
        'optional': [
            "gitpython==3.1.42",
            "qrcode==7.4.2",
            "swissqr==0.2.0"
        ]
    }
)
