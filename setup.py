import sys
from distutils.core import setup, Extension
from glob import glob

sources = glob('src/*')
libraries = []
include_dirs = ['include']

if hasattr(sys, 'getwindowsversion'):
    libraries.extend([ 'rpcrt4', 'ws2_32' ])
    include_dirs.append('include_nt')
else:
    include_dirs.append('include_linux')
    sources.extend(glob('src_uuid/*.c'))

ext = Extension('zmq._zmq', sources, libraries=libraries,
                include_dirs=include_dirs)

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
