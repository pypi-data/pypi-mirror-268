# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lamatrix', 'lamatrix.models']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.26.4,<2.0.0', 'rich>=13.7.1,<14.0.0']

setup_kwargs = {
    'name': 'lamatrix',
    'version': '0.1.0',
    'description': '',
    'long_description': '<a href="https://github.com/christinahedges/lamatrix/actions/workflows/tests.yml"><img src="https://github.com/christinahedges/lamatrix/workflows/pytest/badge.svg" alt="Test status"/></a> [![Generic badge](https://img.shields.io/badge/documentation-live-blue.svg)](https://christinahedges.github.io/lamatrix/)\n[![PyPI version](https://badge.fury.io/py/lamatrix.svg)](https://badge.fury.io/py/lamatrix)\n\n<p align="center">\n  <img src="https://github.com/christinahedges/lamatrix/blob/main/docs/images/logo.png?raw=true" width="350" alt="lamatrix logo">\n</p>\n\n# LAmatrix\n\nThis package is designed to help you fit linear algebra models to data. It\'s designed to eventually replace `Lightkurve.design_matrix` and `Lightkurve.Corrector` objects.\n',
    'author': 'Christina Hedges',
    'author_email': 'christina.l.hedges@nasa.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
