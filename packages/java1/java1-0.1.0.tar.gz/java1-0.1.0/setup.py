# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['java1']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'java1',
    'version': '0.1.0',
    'description': 'A short description of your project',
    'long_description': 'None',
    'author': 'Vinit',
    'author_email': 'suryawanshivinit02@email.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
