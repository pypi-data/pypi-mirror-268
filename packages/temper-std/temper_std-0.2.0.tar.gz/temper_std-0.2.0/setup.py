# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['temper_std']

package_data = \
{'': ['*']}

install_requires = \
['temper-core==0.2.0']

setup_kwargs = {
    'name': 'temper-std',
    'version': '0.2.0',
    'description': 'Optional support library provided with Temper',
    'long_description': 'None',
    'author': 'Temper Contributors',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://temperlang.dev/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
