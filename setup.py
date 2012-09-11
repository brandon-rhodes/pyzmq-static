# -*- coding: utf-8 -*-

import os
from distutils.core import setup

long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')
                        ).read().decode('utf-8')
description = u'Obsolete fork of pyzmq'

setup(name='pyzmq-static',
      version='2.2',
      description=description,
      long_description=long_description,
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      maintainer='Evan Borgstrom',
      maintainer_email='evan@fatbox.ca',
      url='https://github.com/zeromq/pyzmq',

      # Keep people working who depend simply upon 'pyzmq-static'
      # without any version number:

      install_requires = ['pyzmq'],
      )
