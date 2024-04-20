# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cookieplone',
 'cookieplone.filters',
 'cookieplone.utils',
 'cookieplone.utils.commands']

package_data = \
{'': ['*']}

install_requires = \
['cookiecutter>=2.6.0,<3.0.0',
 'packaging>=24.0,<25.0',
 'semver>=3.0.2,<4.0.0',
 'typer[all]>=0.12.3,<0.13.0']

entry_points = \
{'console_scripts': ['cookieplone = cookieplone.__main__:main']}

setup_kwargs = {
    'name': 'cookieplone',
    'version': '0.4.0',
    'description': 'Create Plone projects, addons, documentation with ease!',
    'long_description': '<p align="center">\n    <img alt="Plone Logo" width="200px" src="https://raw.githubusercontent.com/plone/.github/main/plone-logo.png">\n</p>\n\n<h1 align="center">\n  cookieplone\n</h1>\n\n\n<div align="center">\n\n[![PyPI](https://img.shields.io/pypi/v/cookieplone)](https://pypi.org/project/cookieplone/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cookieplone)](https://pypi.org/project/cookieplone/)\n[![PyPI - Wheel](https://img.shields.io/pypi/wheel/cookieplone)](https://pypi.org/project/cookieplone/)\n[![PyPI - License](https://img.shields.io/pypi/l/cookieplone)](https://pypi.org/project/cookieplone/)\n[![PyPI - Status](https://img.shields.io/pypi/status/cookieplone)](https://pypi.org/project/cookieplone/)\n\n\n[![Tests](https://github.com/plone/cookieplone/actions/workflows/main.yml/badge.svg)](https://github.com/plone/cookieplone/actions/workflows/main.yml)\n\n[![GitHub contributors](https://img.shields.io/github/contributors/plone/cookieplone)](https://github.com/plone/cookieplone)\n[![GitHub Repo stars](https://img.shields.io/github/stars/plone/cookieplone?style=social)](https://github.com/plone/cookieplone)\n\n</div>\n',
    'author': 'Plone Community',
    'author_email': 'dev@plone.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/plone/cookieplone',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
