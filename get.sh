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

# Generate platform.hpp from platform.hpp.in
(cd zeromq-2.0.9; ./configure)

# Copy the files we need into our version-controlled directories.
rm -rf include licenses src src_nt zmq
mkdir include licenses src src_nt zmq

cp zeromq-2.0.9/COPYING* \
   licenses

cp util-linux-ng-2.18/shlibs/uuid/src/*.c \
   zeromq-2.0.9/src/*.cpp \
   pyzmq-2.0.7/zmq/_zmq.c \
   src
mv src/gen_uuid_nt.c src_nt
cp util-linux-ng-2.18/shlibs/uuid/src/uuid.sym src_nt

cp util-linux-ng-2.18/shlibs/uuid/src/*.h \
   zeromq-2.0.9/include/*.h* \
   zeromq-2.0.9/src/*.h* \
   pyzmq-2.0.7/zmq/*.h \
   include

cp -r pyzmq-2.0.7/zmq/*.py pyzmq-2.0.7/zmq/eventloop pyzmq-2.0.7/zmq/tests zmq

# Remove the source trees.
#rm -rf pyzmq-2.0.7 util-linux-ng-2.18 zeromq-2.0.9
