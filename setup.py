#!/usr/bin/env python

from distutils.core import setup
from bootstrap import VERSION

setup(name='katello-client-bootstrap',
      version=VERSION,
      description='Bootstrap Script for migrating systems to Foreman & Katello',
      author='Rich Jerrido',
      author_email='rjerrido@outsidaz.org',
      license='GPL-2',
      url='https://github.com/Katello/katello-client-bootstrap',
      scripts=['bootstrap.py'],
      )
