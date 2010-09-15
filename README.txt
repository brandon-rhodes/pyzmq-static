This package provides a statically-linked version
of the ``zmq`` Python library,
which is the official interface between Python
and the `ZeroMQ`_ messaging library.
The official distribution for the ``zmq`` library
is called ``pyzmq`` here on PyPI,
and is maintained by Brian E. Granger:

http://pypi.python.org/pypi/pyzmq/

.. _ZeroMQ: http://www.zeromq.org/

This ``pyzmq-static`` distribution was created by Brandon Craig Rhodes
after he became frustrated with having to install both ``libuuid-dev``
and ZeroMQ itself on every machine where he then wanted to install ``pyzmq``.
Whether you use Linux or Windows,
this package should download and compile with a quick ``pip`` ``install``
assuming that you have the normal tools in place
for building Python extension modules at all
(which are, specifically, the GNU C and C++ compilers for POSIX systems,
and the free Microsoft Visual C++ 2008 Express for Windows machines).

Warning
-------

This Python package is statically linked against ZeroMQ,
which means that it carries its own copy of ZeroMQ around inside of it.

If your Python program imports any other libraries or modules
that themselves link against ZeroMQ,
then they will find themselves talking to a different
copy of the message queue libraries than your program does.
The two copies of ZeroMQ might have different versions;
they might lack shared copies of data structures
that would be necessary to coordinate in-process queues;
or they might break altogether,
depending on how they and your operating system's dynamic linker
decide to behave.

But, this static version has always worked for me so far.

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
