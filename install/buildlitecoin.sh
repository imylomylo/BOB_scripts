#!/bin/bash
curdir=$PWD
cd ~
sudo apt-get update
sudo apt-get install build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils libboost-all-dev git libdb-dev libdb++-dev
git clone https://github.com/litecoin-project/litecoin.git -b 0.15
cd litecoin
./autogen.sh
./configure --without-miniupnpc --without-gui --with-incompatible-bdb
make -j$(nproc)
sudo ln -s /home/$USER/litcoin/src/litecoind /usr/local/bin/litecoind
sudo ln -s /home/$USER/litcoin/src/litecoin-cli /usr/local/bin/litecoin-cli
cd $curdir
./makeconf.sh .litecoin litecoin
