This package provides a statically-linked version
of the **zmq** Python library,
which is the official interface between Python
and the ØMQ messaging library.
You can find the exuberant ØMQ web site here:

http://www.zeromq.org/

The official distribution for the **zmq** library
is called **pyzmq** here on PyPI,
and is maintained by Brian E. Granger:

http://pypi.python.org/pypi/pyzmq/

.. _ZeroMQ: http://www.zeromq.org/

This **pyzmq-static** distribution was created by Brandon Craig Rhodes
after he became frustrated with having to install both libuuid-dev
and ZeroMQ itself on every machine where he then wanted to install **pyzmq**.
Whether you use Linux or Windows,
this package should download and compile with a quick **pip** **install**
assuming that you have the normal tools in place
for building Python extension modules at all
(which are, specifically, the GNU C and C++ compilers for POSIX systems,
and the free Microsoft Visual C++ 2008 Express for Windows machines).

Changelog
---------

| 2.0.8 — 2010-09-27— MacOS X support.
| 2.0.7a — 2010-09-15— World debut!

Warning
-------

This Python package is statically linked against ØMQ:
it carries its own copy of ØMQ around inside of it.
If your Python program imports other libraries or modules
that themselves link against ØMQ,
then linking or runtime problems might arise.

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
working on MacOS X!

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
we will update the *get.sh* script,
tweak the result until it compiles cleanly under Linux and Windows,
and release a new version of **pyzmq-static**.
