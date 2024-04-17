# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['giant_redirect_import', 'giant_redirect_import.tests']

package_data = \
{'': ['*']}

install_requires = \
['django-cms>=3,<4', 'django-import-export>=3.2.0,<4.0.0', 'django>=4.2,<4.3']

setup_kwargs = {
    'name': 'giant-redirect-import',
    'version': '0.8',
    'description': 'Reusable package which adds an option to bulk import redirects from a csv file',
    'long_description': '# Giant Redirect Import\n\nA re-usable package which can be used in any project that requires a Redirect import via a CSV file.\n\nThis will include a basic form to upload a CSV file in the standard `Redirect` app supplied via django.\n\n## Installation\n\nTo install with the package manager, run:\n\n    $ poetry add giant-redirect-import\n\nYou should then add `"giant_redirect_import"` to the `INSTALLED_APPS` in your settings file, this MUST be directly above `django.contrib.redirects`.\n\nIn `base.py` there should also be a `REDIRECT_IMPORT_DEFAULT_SITE_ID`.\n\n\n## Configuration\n\nThis application exposes the following settings:\n\n- `REDIRECT_IMPORT_DEFAULT_SITE_ID` is the default site id used when importing and creating the redirects, this is usually the same as the SITE_ID.\n ## Preparing for release\n \n In order to prep the package for a new release on TestPyPi and PyPi there is one key thing that you need to do. You need to update the version number in the `pyproject.toml`.\n This is so that the package can be published without running into version number conflicts. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.\n \n ## Publishing\n \n Publishing a package with poetry is incredibly easy. Once you have checked that the version number has been updated (not the same as a previous version) then you only need to run two commands.\n \n    $ `poetry build` \n\nwill package the project up for you into a way that can be published.\n \n    $ `poetry publish`\n\nwill publish the package to PyPi. You will need to enter the username and password for the account which can be found in the company password manager\n',
    'author': 'Will-Hoey',
    'author_email': 'will.hoey@hotmail.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/giantmade/giant-redirect-import',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
