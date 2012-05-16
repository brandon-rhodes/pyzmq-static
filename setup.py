# -*- coding: utf-8 -*-
import distutils.util
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
include_dirs = ['include']

if hasattr(sys, 'getwindowsversion'):
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
            '_poll':[czmq, allocate], 
            'stopwatch':[czmq],
            'context':[pxd('core', 'socket'), czmq],
            'message':[czmq, buffers],
            'socket':[pxd('core', 'context'), pxd('core', 'message'), 
                      czmq, allocate, buffers],
            'device':[czmq],
            '_version':[czmq],
    },
    devices = {
            'monitoredqueue':[buffers, czmq],
    },
    utils = {
            'initthreads':[czmq]
    }
)

extensions = [Extension('zmq.libzmq',
                        sources=static_sources,
                        include_dirs=include_dirs)]

for submod, packages in submodules.items():
    for pkg in sorted(packages):
        sources = [pjoin('zmq', submod, pkg+'.c')]
        ext = Extension(
            'zmq.%s.%s'%(submod, pkg),
            sources = sources,
            include_dirs = include_dirs,
        )
        extensions.append(ext)

package_data = {'zmq':['*.pxd'],
                'zmq.core':['*.pxd'],
                'zmq.devices':['*.pxd'],
                'zmq.utils':['*.pxd', '*.h'],
}

# Visual Studio needs some encouragement to actually compile everything.

if hasattr(sys, 'getwindowsversion'):

    libzmq = extensions[0]
    other_extensions = extensions[1:]

    # When compiling the C++ code inside of libzmq itself, we want to
    # avoid "warning C4530: C++ exception handler used, but unwind
    # semantics are not enabled. Specify /EHsc".

    libzmq.extra_compile_args.append('/EHsc')

    # Because Visual Studio is given the option "/EXPORT:initlibzmq"
    # when compiling libzmq, so we need to provide such a function.

    libzmq.sources.append(r'src_nt\initlibzmq.c')

    # And things like sockets come from libraries that must be named.

    libzmq.libraries.append('rpcrt4')
    libzmq.libraries.append('ws2_32')

    # Then all of the real extensions need to link against that first
    # library.

    plat = distutils.util.get_platform()
    temp = 'temp.%s-%s' % (plat, sys.version[0:3])
    for other in other_extensions:
        thisdir = os.path.dirname(__file__)
        libdir = os.path.join(thisdir, 'build', temp, 'Release', 'src')
        other.library_dirs.append(libdir)
        other.libraries.append('libzmq')

# The setup() call itself.

long_description = open('README.rst').read().decode('utf-8')
if sys.version_info < (2, 6):  # work around Python 2.5 UnicodeEncodeError
    description = u'zmq package that compiles its own 0MQ / ZeroMQ'
    long_description = long_description.encode('utf-8')
else:
    description = u'zmq package that compiles its own ØMQ / 0MQ / ZeroMQ'

setup(name='pyzmq-static',
      version='2.1.11.1',
      description=description,
      long_description=long_description,
      author='Brandon Craig Rhodes',
      author_email='brandon@rhodesmill.org',
      maintainer='Evan Borgstrom',
      maintainer_email='evan@fatbox.ca',
      url='https://github.com/brandon-rhodes/pyzmq-static',
      cmdclass = cmdclass,
      packages = ['zmq', 'zmq.tests', 'zmq.eventloop', 'zmq.log', 'zmq.core',
                  'zmq.devices', 'zmq.utils', 'zmq.web'],
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
