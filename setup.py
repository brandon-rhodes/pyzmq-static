import os
import sys
from distutils.core import setup, Extension
from glob import glob

sources = glob('src/*')
include_dirs = ['include']
extra_link_args = []

if hasattr(sys, 'getwindowsversion'):
    sources.extend(glob('src_nt/*.c'))
    include_dirs.insert(0, 'include_nt')  # prepend so its files are used first
    extra_link_args.append('-Wl,--version-script=src_nt/uuid.sym')

ext = Extension('zmq._zmq', sources, include_dirs=include_dirs,
                extra_link_args=extra_link_args)

setup(name='pyzmq-static',
      version='2.0.7a',
      description='Official interface statically linked against 0MQ',
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      url='http://bitbucket.org/brandon/pyzmq-static',
      packages=['zmq'],
      package_dir={'zmq': os.path.join('pyzmq-2.0.7', 'zmq')},
      ext_modules=[ ext ],
      )
