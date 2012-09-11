# -*- coding: utf-8 -*-

from distutils.core import setup

long_description = open('README.rst').read().decode('utf-8')
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

      # Should we release a 2.2 tarball consisting only of the README
      # and the following requirement, so that users get automatically
      # migrated over if they did not pin their pyzmq-static version?
      #
      # install_requires = ['pyzmq'],
      )
