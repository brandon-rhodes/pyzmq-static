import os
from distutils.core import setup, Extension

def _(path):
    return os.path.join(*path.split('/'))

setup(name='pyzmq-static',
      version='2.0.7a',
      description='Official interface statically linked against 0MQ',
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      url='http://bitbucket.org/brandon/pyzmq-static',
      packages=['zmq'],
      package_dir={'zmq': _('pyzmq-2.0.7/zmq')},
      ext_modules=[
        #Extension('foo', ['foo.c'])
        ],
      )
