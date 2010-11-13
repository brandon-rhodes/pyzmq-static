#!/bin/bash

# Die on error
set -e

# Re-fetch the sources necessary for building pyzmq-static.
cd $(dirname "$0")
mkdir -p tmp

UTIL=util-linux-ng-2.18
ZEROMQ=zeromq-2.0.10
PYZMQ=pyzmq-2.0.8

# Download source distributions, or make sure they are up to date.
cd tmp
wget -c "http://www.kernel.org/pub/linux/utils/util-linux-ng/v2.18/$UTIL.tar.gz"
wget -c "http://www.zeromq.org/local--files/area:download/$ZEROMQ.tar.gz"
wget -c "http://pypi.python.org/packages/source/p/pyzmq/$PYZMQ.tar.gz#md5=b21ab6bc336c211c504068ecc55bc5cf"
cd ..

# Untar them.
tar xvfz tmp/$UTIL.tar.gz
tar xvfz tmp/$ZEROMQ.tar.gz
tar xvfz tmp/$PYZMQ.tar.gz

# Copy the files we need into our version-controlled directories.  (We
# keep include_linux and include_darwin from one run to the next, since
# we cannot replace their contents unless we are on that platform.)
rm -rf include licenses src src_nt src_uuid zmq
mkdir include licenses src src_nt src_uuid zmq

cp $ZEROMQ/COPYING* \
   licenses

cp $ZEROMQ/src/*.cpp \
   $PYZMQ/zmq/_zmq.c \
   src
cp $UTIL/shlibs/uuid/src/*.c \
   src_uuid
rm src_uuid/gen_uuid_nt.c

cp $UTIL/shlibs/uuid/src/*.h \
   $ZEROMQ/include/*.h* \
   $ZEROMQ/src/*.h* \
   $PYZMQ/zmq/*.h \
   include

cp -r $PYZMQ/zmq/*.py $PYZMQ/zmq/eventloop $PYZMQ/zmq/tests zmq

# Generate platform.hpp from platform.hpp.in so that I can compare it
# against the cached versions.

(cd $ZEROMQ; ./configure)
cp $ZEROMQ/src/platform.hpp .

# Remove the source trees.
rm -rf $PYZMQ $UTIL $ZEROMQ
