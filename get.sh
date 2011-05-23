#!/bin/bash

# Die on error

set -e

# Re-fetch the sources necessary for building pyzmq-static.

cd $(dirname "$0")

UTIL=util-linux-2.19
ZEROMQ=zeromq-2.1.7
PYZMQ=pyzmq-2.1.7

# Download source distributions, or make sure they are up to date.

if [ ! -d tmp ]; then
    mkdir tmp
    cd tmp
    curl -O "http://www.kernel.org/pub/linux/utils/util-linux-ng/v2.19/$UTIL.tar.gz"
    curl -O "http://download.zeromq.org/$ZEROMQ.tar.gz"
    curl -O "http://pypi.python.org/packages/source/p/pyzmq/$PYZMQ.tar.gz"
    cd ..
fi

# Untar them.

tar xvfz tmp/$UTIL.tar.gz
tar xvfz tmp/$ZEROMQ.tar.gz
tar xvfz tmp/$PYZMQ.tar.gz

# Copy the files we need into our version-controlled directories.  (We
# keep include_linux and include_darwin from one run to the next, since
# we cannot replace their contents unless we are on that platform.)

rm -rf include include_uuid licenses src src_nt src_uuid zmq
mkdir  include include_uuid licenses src src_nt src_uuid zmq

cp $ZEROMQ/COPYING* \
   licenses

cp $ZEROMQ/src/*.cpp \
   src
cp $UTIL/shlibs/uuid/src/*.c \
   src_uuid
rm src_uuid/gen_uuid_nt.c

cp $ZEROMQ/include/*.h* \
   $ZEROMQ/src/*.h* \
   $PYZMQ/zmq/utils/*.h \
   include

mkdir include_uuid/uuid
cp $UTIL/shlibs/uuid/src/*.h include_uuid      # where uuid expects it
cp $UTIL/shlibs/uuid/src/*.h include_uuid/uuid # where ZeroMQ expects it

(cd $PYZMQ/zmq; tar cf - *.py */*.py */*.c) | (cd zmq; tar xf -)

cp $ZEROMQ/builds/msvc/platform.hpp include_nt

# Patch gen_uuid.c so that it gets some header files it needs.
# Patch pyzmq to manually load the 0MQ shared library.

patch -p0 < patch-gen_uuid
patch -p0 < patch-zmq-init

# Generate platform.hpp from platform.hpp.in so that I can compare it
# against the cached versions.

(cd $ZEROMQ; ./configure)
cp $ZEROMQ/src/platform.hpp .

# Remove the source trees.

rm -rf $PYZMQ $UTIL $ZEROMQ
