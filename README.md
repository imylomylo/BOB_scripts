 Scripts for creating a BOB node for BarterDEX

## Installing MarketMaker
1) Create a VPS (depending on how many coins you will run determines the size, 2 coins 2GB ram is fine)
2) Add yourself a user and give it sudo access, if you want secure it with a SSH key pair.
3) install git: `sudo apt-get install git`
4) clone this repo: `git clone https://github.com/blackjok3rtt/BOB_scripts.git`
5) `cd ~/BOB_scripts/install`
6) `./install.sh`
7) If you are using komodo and its assets install it: `./buildkomodo.sh`
8) `cd ~/BOB_scripts/vps_scripts`
9) Install and start all coin deamons you are going to use
10) `./start`

## Installing Local Copy to your Linux Computer
This part of the guide will need updating. We should make a simple GUI for managing a while bunch of marketmakers with just a few clicks.
1) install git
2) `git clone https://github.com/blackjok3rtt/BOB_scripts.git`
3) `cd BOB_scripts/scripts`
4) edit the passprase file with the passphrase your bob will use
5) edit the sshtunnel file to point to the user@"yourvps"
6) `./sshtunnel`
7) `./login.sh`


