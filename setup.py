# Copyright (c) 2016-2019 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import json

from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'fuzzinator', 'PKGDATA.json'), 'r') as f:
    data = json.load(f)

setup(
    name=data['name'],
    version=data['version'],
    packages=find_packages(),
    url=data['url'],
    license='BSD',
    author=data['author'],
    author_email=data['author_email'],
    description='Fuzzinator Random Testing Framework',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'chardet',
        'chevron',
        'google-api-python-client',
        'jinja2',
        'keyring',
        'keyrings.alt',
        'markdown',
        'oauth2client',
        'pexpect',
        'picire==19.3',
        'picireny==19.3',
        'psutil',
        'PyGithub',
        'pymongo',
        'pyperclip',
        'python-bugzilla',
        'python-gitlab',
        'rainbow_logging_handler',
        'setuptools',
        'sphinx',
        'sphinx_rtd_theme',
        'tornado<6.0',  # no Tornado 6 for Python < 3.5
        'urwid',
    ],
    entry_points={
        'console_scripts': ['fuzzinator = fuzzinator.executor:execute']
    }
)
