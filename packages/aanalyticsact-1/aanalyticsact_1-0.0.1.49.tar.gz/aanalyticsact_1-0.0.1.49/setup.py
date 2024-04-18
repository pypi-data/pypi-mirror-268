#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'aanalyticsact_1'
Version= '0.0.1.49'
URL = 'https://github.com/Glory-Cho/aanalyticsact)1'
Summary= 'adobe analytics library for Team ACT'
EMAIL = 'youngkwang.cho@concentrix.com'
AUTHOR = 'Youngkwang Cho'

here = os.path.abspath(os.path.dirname(__file__))

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()


setup(
    name=NAME,
    version = Version,
    summary=Summary,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    license='',
)