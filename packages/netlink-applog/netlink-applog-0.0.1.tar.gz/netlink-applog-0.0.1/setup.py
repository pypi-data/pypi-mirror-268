# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['applog']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'netlink-applog',
    'version': '0.0.1',
    'description': 'Logging to a SQLite Database',
    'long_description': None,
    'author': 'Bernhard Radermacher',
    'author_email': 'bernhard.radermacher@netlink-consulting.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/netlink_python/netlink-applog.git',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<3.13',
}


setup(**setup_kwargs)
