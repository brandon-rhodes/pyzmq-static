#!/bin/bash

# Die on error

set -e

# Re-fetch the sources necessary for building pyzmq-static.

cd $(dirname "$0")

UTIL=util-linux-2.21
ZEROMQ=zeromq-2.2.0
PYZMQ=pyzmq-2.2.0

# Download source distributions, or make sure they are up to date.

if [ ! -d tmp ]; then
    mkdir tmp
    cd tmp
    curl -L -O "http://mirror.anl.gov/pub/linux/utils/util-linux/v2.21/$UTIL.tar.gz"
    curl -L -O "http://download.zeromq.org/$ZEROMQ.tar.gz"
    curl -L -O "https://github.com/zeromq/pyzmq/downloads/$PYZMQ.tar.gz"
    cd ..
fi

# Untar them.

tar xvfz tmp/$UTIL.tar.gz
tar xvfz tmp/$ZEROMQ.tar.gz
tar xvfz tmp/$PYZMQ.tar.gz

# Copy the files we need into our version-controlled directories.  (We
# keep include_linux and include_darwin from one run to the next, since
# we cannot replace their contents unless we are on that platform.)

rm -rf include include_uuid licenses src src_uuid zmq
mkdir  include include_uuid licenses src src_uuid zmq

cp $ZEROMQ/COPYING* \
   licenses

cp $ZEROMQ/src/*.cpp \
   src

cp $UTIL/libuuid/src/*.c \
   src_uuid
rm src_uuid/gen_uuid_nt.c

cp $ZEROMQ/include/*.h* \
   $ZEROMQ/src/*.h* \
   $PYZMQ/zmq/utils/*.h \
   include

mkdir include_uuid/uuid
cp $UTIL/libuuid/src/*.h include_uuid      # where uuid expects it
cp $UTIL/libuuid/src/*.h include_uuid/uuid # where ZeroMQ expects it

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
