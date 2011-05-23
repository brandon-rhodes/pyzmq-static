This package combines the **zmq** Python package
with a bundled copy of ØMQ
so that you do not have to install ØMQ separately on your system.
This version combines:

* ØMQ 2.1.7 — http://www.zeromq.org/
* PyZMQ 2.1.7 — http://pypi.python.org/pypi/pyzmq/

On Linux and MacOS systems (but not on Windows or FreeBSD),
the ``libuuid`` library code is also compiled in:

* util-linux-ng 2.19 — http://www.kernel.org/pub/linux/utils/util-linux-ng/

PyZMQ is the official interface between Python
and the ØMQ messaging library.
The official distribution is called **pyzmq** on PyPI,
and is maintained by Brian E. Granger.

This **pyzmq-static** distribution was created by Brandon Craig Rhodes
after he became frustrated with having to install both libuuid-dev
and ZeroMQ itself on every machine where he then wanted to install **pyzmq**.
Whether you use Linux or Windows,
this package should download and compile with a quick **pip** **install**
without requiring any dependencies beyond the normal tools
for building Python extension modules at all
(which are, specifically, the GNU C and C++ compilers for POSIX systems,
and the free Microsoft Visual C++ 2008 Express for Windows machines).

Changelog
---------

| 2011-05-22 — 2.1.7 — ØMQ and PyZMQ 2.1.7.
| 2011-04-02 — 2.1.4 — ØMQ 2.1.4; PyZMQ 2.1.1; util-linux-ng 2.19.
| 2010-11-17 — 2.0.10 — ØMQ 2.0.10; FreeBSD support.
| 2010-09-27 — 2.0.8 — Mac OS X support.
| 2010-09-15 — 2.0.7a — World debut!

Copying
-------

This package uses a "setup.py" file,
which Brandon Craig Rhodes happily offers under a BSD license,
to build a shared library built from three different source distributions.
To use the result, you must adhere to the licensing terms of all three
pieces of software, which are as follows:

* The UUID routines from "util-linux-ng": BSD
* The "zeromq" source: LGPL
* The "pyzmq" source: LGPL

So, okay, those are not very restrictive licensing terms.
But still.
See the source files themselves for more information.
And thanks to Jeff Garbers for helping me get the package
working on MacOS X;
to Tyler Tarabula for the FreeBSD support;
and to Benjamin RK for helping me rewrite ``setup.py``
when PyZMQ split from being one C extension to almost a dozen!

Development
-----------

The source of **pyzmq-static** lives at Bitbucket:

http://bitbucket.org/brandon/pyzmq-static

You can report bugs and problems,
which Bitbucket euphemistically calls "issues",
here:

http://bitbucket.org/brandon/pyzmq-static/issues

The development tree is accompanied by a small *get.sh* shell script
that re-fetches all of the original source distributions
for ØMQ, pyzmq, and libuuid, and rebuilds the *include* and *src*
directories using the original files.
When new versions of these dependencies come out,
I update the *get.sh* script,
tweak the result until it compiles cleanly under Linux and Windows,
and release a new version of **pyzmq-static**.
