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
