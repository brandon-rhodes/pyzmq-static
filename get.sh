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
wget -c "http://pypi.python.org/packages/source/p/pyzmq/pyzmq-2.0.7.tar.gz#md5=1f563a7719deda735fa853a995971fe9"
cd ..

# Untar them.
tar xvfz tmp/util-linux-ng-2.18.tar.gz
tar xvfz tmp/zeromq-2.0.9.tar.gz
tar xvfz tmp/pyzmq-2.0.7.tar.gz

# Copy the files we need into our version-controlled directories.  (We
# keep include_linux and include_darwin from one run to the next, since
# we cannot replace their contents unless we are on that platform.)
rm -rf include include_nt licenses src src_nt src_uuid zmq
mkdir include include_nt licenses src src_nt src_uuid zmq

cp zeromq-2.0.9/COPYING* \
   licenses

cp zeromq-2.0.9/src/*.cpp \
   pyzmq-2.0.7/zmq/_zmq.c \
   src
cp util-linux-ng-2.18/shlibs/uuid/src/*.c \
   src_uuid
rm src_uuid/gen_uuid_nt.c

cp util-linux-ng-2.18/shlibs/uuid/src/*.h \
   zeromq-2.0.9/include/*.h* \
   zeromq-2.0.9/src/*.h* \
   pyzmq-2.0.7/zmq/*.h \
   include
rm include/platform.hpp

cp -r pyzmq-2.0.7/zmq/*.py pyzmq-2.0.7/zmq/eventloop pyzmq-2.0.7/zmq/tests zmq

# Generate platform.hpp from platform.hpp.in
(cd zeromq-2.0.9; ./configure)
case $(uname) in
    Linux)
        mkdir -p include_linux
        cp zeromq-2.0.9/src/platform.hpp include_linux
    ;;
    Darwin)
        mkdir -p include_darwin
        cp zeromq-2.0.9/src/platform.hpp include_darwin
    ;;
esac

# Or copy it for Windows
cp zeromq-2.0.9/builds/msvc/platform.hpp include_nt

# Remove the source trees.
rm -rf pyzmq-2.0.7 util-linux-ng-2.18 zeromq-2.0.9
