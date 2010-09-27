#!/bin/bash

# Die on error
set -e

# Re-fetch the sources necessary for building pyzmq-static.
cd $(dirname "$0")
mkdir -p tmp

# Download source distributions, or make sure they are up to date.
cd tmp
wget -c "http://www.kernel.org/pub/linux/utils/util-linux-ng/v2.18/util-linux-ng-2.18.tar.gz"
wget -c "http://www.zeromq.org/local--files/area:download/zeromq-2.0.9.tar.gz"
wget -c "http://pypi.python.org/packages/source/p/pyzmq/pyzmq-2.0.8.tar.gz#md5=b21ab6bc336c211c504068ecc55bc5cf"
cd ..

# Untar them.
tar xvfz tmp/util-linux-ng-2.18.tar.gz
tar xvfz tmp/zeromq-2.0.9.tar.gz
tar xvfz tmp/pyzmq-2.0.8.tar.gz

UTIL=util-linux-ng-2.18
ZEROMQ=zeromq-2.0.9
PYZMQ=pyzmq-2.0.8

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

# # Generate platform.hpp from platform.hpp.in
# (cd $ZEROMQ; ./configure)
# case $(uname) in
#     Linux)
#         mkdir -p include_linux
#         cp $ZEROMQ/src/platform.hpp include_linux
#     ;;
# esac

# # Or copy it for Windows
# cp $ZEROMQ/builds/msvc/platform.hpp include_nt

# Remove the source trees.
rm -rf $PYZMQ $UTIL $ZEROMQ
