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
      description='Statically linked Python bindings for 0MQ',
      long_description=open('README.rst').read(),
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      url='http://bitbucket.org/brandon/pyzmq-static',
      packages = ['zmq', 'zmq.tests', 'zmq.eventloop'],
      ext_modules=[ ext ],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        #'Operating System :: MacOS :: MacOS X',  # must test!
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: System :: Networking'
        ]
      )
