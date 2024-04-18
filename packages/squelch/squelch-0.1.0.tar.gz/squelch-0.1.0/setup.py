# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['squelch']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy>=2.0.29,<3.0.0', 'tabulate>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['squelch = squelch.__main__:main']}

setup_kwargs = {
    'name': 'squelch',
    'version': '0.1.0',
    'description': 'Simple SQL REPL Command Handler',
    'long_description': '# squelch\n\nSquelch is a package providing a Simple SQL REPL Command Handler.  Squelch uses SQLAlchemy for database access and so can support any database engine that SQLAlchemy supports, thereby providing a common database client experience for any of those database engines.  Squelch is modelled on a simplified `psql`, the PostgreSQL command line client.  The Squelch CLI supports readline history and basic SQL statement tab completions.\n\n',
    'author': 'Paul Breen',
    'author_email': 'pbree@bas.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
