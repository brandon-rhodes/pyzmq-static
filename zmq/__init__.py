"""Python bindings for 0MQ."""

#
#    Copyright (c) 2010 Brian E. Granger
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import sys

import ctypes, os
here = os.path.dirname(__file__)
if sys.platform.startswith('win'):
    # In Windows the library might be a DLL or disguised as a Python
    # extension.  If we cannot find either, we simply keep going without
    # complaint, in the hope that the application has loaded it through
    # some other mechanism.
    libzmq = os.path.join(here, 'libzmq.dll')
    if not os.path.exists(libzmq):
        libzmq = os.path.join(here, 'libzmq.pyd')
    if os.path.exists(libzmq):
        ctypes.cdll.LoadLibrary(libzmq)
else:
    # Under Linux, we cannot use "import" if we need the other extension
    # modules we load to be able to see symbols inside of "libzmq"; so
    # we load the shared library manually, using RTLD_GLOBAL.
    libzmq = os.path.join(here, 'libzmq.so')
    ctypes.CDLL(libzmq, mode=ctypes.RTLD_GLOBAL)
del here, libzmq, ctypes, os

from zmq.utils import initthreads # initialize threads
initthreads.init_threads()

from zmq import core, devices
from zmq.core import *

def get_includes():
    """Return a list of directories to include for linking against pyzmq with cython."""
    from os.path import join, dirname, abspath, pardir
    base = dirname(__file__)
    parent = abspath(join(base, pardir))
    return [ parent ] + [ join(base, subdir) for subdir in ('utils',) ]


__all__ = ['get_includes'] + core.__all__

