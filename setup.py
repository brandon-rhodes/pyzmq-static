import os
import sys
from distutils.core import setup, Extension
from glob import glob

def _(path):
    return glob(os.path.join(*path.split('/')))

sources = (
    _('uuid/*.c') +
    _('zeromq-2.0.9/src/*.cpp') +
    _('pyzmq-2.0.7/zmq/_zmq.c')
    )
include_dirs = (
    _('util-linux-ng-2.18/shlibs/uuid/src/') +
    _('zeromq-2.0.9/include')
    )
extra_link_args = []

if hasattr(sys, 'getwindowsversion'):
    sources.extend(_('uuid-nt/*.c'))
    extra_link_args.append(
        '-Wl,--version-script=$(ul_libuuid_srcdir)/uuid.sym'
        )

ext = Extension('zmq._zmq', sources, include_dirs,
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
