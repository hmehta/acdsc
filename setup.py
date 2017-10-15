#!/usr/bin/python3

import sys

from setuptools import setup, find_packages

install_requires = ['click']
scripts = ['acdsc']

setup(name='acdsc',
      version='0.0.1alpha',
      description='Assetto Corsa Dedicated Server Control',
      url='http://TBD',
      author='Heikki Mehtänen',
      author_email='heikki@mehtanen.fi',
      license='Beerware',
      install_requires=install_requires,
      scripts=scripts)
