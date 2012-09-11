**We bring you good news!**

The official maintainer of the Python
`pyzmq <http://pypi.python.org/pypi/pyzmq/>`_ package,
`@minrk <https://github.com/minrk>`_,
has `merged our work <https://github.com/zeromq/pyzmq/pull/205>`_
into the main project!

That's right — the official version of PyZMQ
can now detect the absence of a system-wide ØMQ library
and respond by building and linking to its own copy of the library.
The PyZMQ distribution carries its own copy of the source code
so that no network access is necessary
for its install to complete successfully.

This means your project can now simply depend upon normal ``pyzmq``
instead of the separate name ``pyzmq-static``.

The main PyZMQ gained this superpower with its 2.2.0.1 release.
If you need to use an older version of PyZMQ,
then you can simply hard-code a dependency
in your ``requirements.txt`` or ``setup.py``
against whatever older version of ``pyzmq-static``
you would like to keep using::

    pyzmq-static==2.1.11.2

Thanks again to `Evan Borgstrom <https://github.com/borgstrom>`_
for helping me (`Brandon Rhodes <https://github.com/brandon_rhodes>`_)
maintain this project,
and thanks to our users for letting us know
how often this distribution of ``pyzmq`` helped you get off the ground!

Changelog
---------

| 2012-08-20 — Project end — `@minrk`_ merges our work!
| 2012-04-28 — 2.1.11 — ØMQ and PyZMQ 2.1.11
| 2011-06-15 — 2.1.7.1 — Fixed compilation under Windows.
| 2011-05-22 — 2.1.7 — ØMQ and PyZMQ 2.1.7.
| 2011-04-02 — 2.1.4 — ØMQ 2.1.4; PyZMQ 2.1.1; util-linux-ng 2.19.
| 2010-11-17 — 2.0.10 — ØMQ 2.0.10; FreeBSD support.
| 2010-09-27 — 2.0.8 — Mac OS X support.
| 2010-09-15 — 2.0.7a — World debut!
