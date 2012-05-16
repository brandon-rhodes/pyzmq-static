pyzmq-static
============

Self contained version of the ØMQ & PyZMQ libraries that download,
compile & install with a single command. See the Quickstart.

Current Version
---------------

This version combines:

* ØMQ 2.2.0 — http://www.zeromq.org/
* PyZMQ 2.2.0 — http://www.zeromq.org/bindings:python/

On Linux and MacOS systems (but not on Windows or FreeBSD), the ``libuuid``
library code is also compiled in from:

* util-linux-ng 2.21 — http://mirror.anl.gov/pub/linux/utils/util-linux

Quickstart
----------

    pip install pyzmq-static

On Linux, Windows, FreeBSD or Mac OS X this will download and compile
a fully self contained installation of zmq & pyzmq without requiring
any dependencies beyond the normal tools for building Python extension
modules. On POSIX systems this means you need the GNU C and C++
compilers on Windows machines you'll need free Microsoft Visual C++
Express version that was used to compile Python (If you're using the
binary 2.7 dist from python.org this means you need VC++ Express 2008)

Overview
--------

This package combines the **zmq** Python package with a bundled copy of
ØMQ so that you do not have to install ØMQ separately on your system.

PyZMQ is the official interface between Python and the ØMQ messaging
library. The official distribution is called **pyzmq** on PyPI, and is
maintained by Brian E. Granger.

This **pyzmq-static** distribution was created by Brandon Rhodes after
he became frustrated with having to install both libuuid-dev and ZeroMQ
itself on every machine where he then wanted to install **pyzmq**. It is
now maintained by Evan Borgstrom (@borgstrom on github).


Copying
-------

The `setup.py` and `get.sh` files that power this package are offered
under the BSD license. They build a shared library that includes code
from the different pieces of software. To use the resulting library,
you must adhere to the licensing terms of all three projects, which are
as follows:

* The UUID routines from "util-linux-ng": BSD
* The "zeromq" source: LGPL
* The "pyzmq" source: LGPL

So, okay, those are not very restrictive licensing terms. But still...
See the source files themselves for more information.


Thanks
------

* Jeff Garbers for helping get the package working on MacOS X
* Tyler Tarabula for the FreeBSD support
* Benjamin RK for help rewriting `setup.py` when PyZMQ split from being
  one C extension to almost a dozen!
* David Bishop for the Debian packaging files

Development
-----------

The source of **pyzmq-static** lives at GitHub:

https://github.com/brandon-rhodes/pyzmq-static

You can report bugs and problems here:

https://github.com/brandon-rhodes/pyzmq-static/issues

The `master` branch contains the version that is currently published
at the cheeseshop: http://pypi.python.org/pypi/pyzmq-static

The `develop` branch contains the current work in progress version.
