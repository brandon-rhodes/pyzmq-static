# -*- coding: utf-8 -*-
#import setuptools
import os
import sys
from distutils.core import setup, Extension, Command
from glob import glob

from traceback import print_exc
from unittest import TextTestRunner, TestLoader
from os.path import splitext, basename, join as pjoin

try:
    import nose
except ImportError:
    nose = None

#-----------------------------------------------------------------------------
# Extra commands
#-----------------------------------------------------------------------------

class TestCommand(Command):
    """Custom distutils command to run the test suite."""

    user_options = [ ]

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass
    
    def run_nose(self):
        """Run the test suite with nose."""
        return nose.core.TestProgram(argv=["", '-vvs', pjoin(self._dir, 'zmq', 'tests')])
    
    def run_unittest(self):
        """Finds all the tests modules in zmq/tests/ and runs them."""
        testfiles = [ ]
        for t in glob(pjoin(self._dir, 'zmq', 'tests', '*.py')):
            name = splitext(basename(t))[0]
            if name.startswith('test_'):
                testfiles.append('.'.join(
                    ['zmq.tests', name])
                )
        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity = 2)
        t.run(tests)
    
    def run(self):
        """Run the test suite, with nose, or unittest if nose is unavailable"""
        # crude check for inplace build:
        try:
            import zmq
        except ImportError:
            print_exc()
            print ("Could not import zmq!")
            print ("You must build pyzmq with 'python setup.py build_ext --inplace' for 'python setup.py test' to work.")
            print ("If you did build pyzmq in-place, then this is a real error.")
            sys.exit(1)
        
        if nose is None:
            print ("nose unavailable, falling back on unittest. Skipped tests will appear as ERRORs.")
            return self.run_unittest()
        else:
            return self.run_nose()

cmdclass = {'test':TestCommand}

#-----------------------------------------------------------------------------
# Static linking extras
#-----------------------------------------------------------------------------

static_sources = glob('src/*')
libraries = []
include_dirs = ['include']

if hasattr(sys, 'getwindowsversion'):
    libraries.extend([ 'rpcrt4', 'ws2_32' ])
    include_dirs.append('include_nt')
else:
    if sys.platform == 'darwin':
        include_dirs.append('include_macosx')
        include_dirs.append('include_uuid')
        static_sources.extend(glob('src_uuid/*.c'))
    elif sys.platform.startswith('freebsd'):  # for example, 'freebsd7'
        include_dirs.append('include_freebsd')
    else:
        include_dirs.append('include_linux')
        include_dirs.append('include_uuid')
        static_sources.extend(glob('src_uuid/*.c'))

#-----------------------------------------------------------------------------
# Extensions
#-----------------------------------------------------------------------------

include_dirs.append(pjoin('zmq', 'utils'))

def pxd(subdir, name):
    return os.path.abspath(pjoin('zmq', subdir, name+'.pxd'))

czmq = pxd('core', 'czmq')
allocate = pxd('utils', 'allocate')
buffers = pxd('utils', 'buffers')

submodules = dict(
    core = {'constants': [czmq],
            'error':[czmq],
            'poll':[czmq, allocate], 
            'stopwatch':[czmq],
            'context':[pxd('core', 'socket'), czmq],
            'message':[czmq, buffers],
            'socket':[pxd('core', 'context'), pxd('core', 'message'), 
                      czmq, allocate, buffers],
            'device':[czmq],
            'version':[czmq],
    },
    devices = {
            'monitoredqueue':[buffers, czmq],
    },
    utils = {
            'initthreads':[czmq]
    }
)

extensions = []
for submod, packages in submodules.items():
    for pkg in sorted(packages):
        sources = [pjoin('zmq', submod, pkg+'.c')]
        ext = Extension(
            'zmq.%s.%s'%(submod, pkg),
            sources = sources,
            include_dirs = include_dirs,
        )
        extensions.append(ext)

extensions.append(Extension('zmq._zeromq',
                            sources=static_sources,
                            include_dirs=include_dirs))

package_data = {'zmq':['*.pxd'],
                'zmq.core':['*.pxd'],
                'zmq.devices':['*.pxd'],
                'zmq.utils':['*.pxd', '*.h'],
}

long_description = open('README.txt').read().decode('utf-8')
if sys.version_info < (2, 6):  # work around Python 2.5 UnicodeEncodeError
    description = u'zmq package that compiles its own 0MQ / ZeroMQ'
    long_description = long_description.encode('utf-8')
else:
    description = u'zmq package that compiles its own ØMQ / 0MQ / ZeroMQ'

setup(name='pyzmq-static',
      version='2.1.7',
      description=description,
      long_description=long_description,
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      url='http://bitbucket.org/brandon/pyzmq-static',
      cmdclass = cmdclass,
      packages = ['zmq', 'zmq.tests', 'zmq.eventloop', 'zmq.log', 'zmq.core',
                  'zmq.devices', 'zmq.utils'],
      package_data = package_data,
      ext_modules= extensions,
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: MacOS :: MacOS X',  # passes tests
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: System :: Networking'
        ]
      )
