#!/bin/sh

pip3 -V > /dev/null || (echo 'Error: Unable to find pip3. Aborting.' && exit 1)

thisdir=$(pwd)

cd /
pip3 install $thisdir
cd -

install -D app/autotype /usr/bin
