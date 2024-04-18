try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Mondata, a data-driven client for Monday.com',
    'author': 'Andrew Shatz',
    'url': r'https://github.com/Great-Strength-Studios/mondata',
    'download_url': r'https://github.com/Great-Strength-Studios/mondata',
    'author_email': 'andrew@greatstrength.me',
    'version': '1.0.0-alpha',
    'license': 'BSD 3',
    'install_requires': [
        'requests>=2.31.0',
        'pytz>=2024.1',
        'pycountry>=23.12.11',
        'deprecated>=1.2.14',
        'schematics>=2.1.1'
    ],
    'tests_require': [
        'nose>=1.3.7'
    ],
    'packages': [
        'mondata',
        'mondata.api_v2',
        'mondata.entities',
        'mondata.column_value'
    ],    
    'scripts': [],
    'name': 'mondata'
}

setup(**config)
