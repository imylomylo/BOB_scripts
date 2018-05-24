#!/bin/bash
curdir=$PWD
cd ~
sudo apt-get update
sudo apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils libboost-all-dev git libdb-dev libdb++-dev
git clone https://github.com/dashpay/dash.git
cd dash
./autogen.sh
./configure --without-miniupnpc --without-gui --with-incompatible-bdb
make -j$(nproc)
sudo ln -s /home/$USER/dash/src/dashd /usr/local/bin/dashd
sudo ln -s /home/$USER/dash/src/dash-cli /usr/local/bin/dash-cli
cd $curdir
./makeconf.sh .dashcore dash
