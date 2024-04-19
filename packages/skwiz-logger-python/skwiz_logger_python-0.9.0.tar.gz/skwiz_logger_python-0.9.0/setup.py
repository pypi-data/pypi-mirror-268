# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skwiz_logger_python']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'skwiz-logger-python',
    'version': '0.9.0',
    'description': 'A saga logger for python projects',
    'long_description': 'None',
    'author': 'hmoumal',
    'author_email': 'henri.moumal@sagacify.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
