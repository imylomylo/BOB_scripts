#Install Deps
curdir=$PWD
sudo apt-get update
sudo apt-get install build-essential pkg-config libc6-dev m4 g++-multilib autoconf libcurl4-gnutls-dev libtool ncurses-dev unzip git python python-zmq zlib1g-dev wget libcurl3-gnutls-dev bsdmainutils automake curl
#Install Komodo
cd ~
git clone https://github.com/jl777/komodo -b dev
cd komodo
./zcutil/fetch-params.sh
./zcutil/build.sh -j$(nproc)
sudo ln -sf /home/$USER/komodo/src/komodo-cli /usr/local/bin/komodo-cli
sudo ln -sf /home/$USER/komodo/src/komodod /usr/local/bin/komodod
cd $curdir
./makeconf.sh .komodo komodo
