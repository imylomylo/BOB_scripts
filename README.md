 Scripts for creating a BOB node for BarterDEX

## Installing MarketMaker
1) Create a VPS (depending on how many coins you will run determines the size, 2 coins 2GB ram is fine)
2) Add yourself a user and give it sudo access, I strongly suggest using an SSH key pair with no password.
3) install git: `sudo apt-get install git`
4) clone this repo: `git clone https://github.com/blackjok3rtt/BOB_scripts.git`
5) `cd ~/BOB_scripts/install`
6) `./install.sh`
7) If you are using komodo and its assets install it: `./buildkomodo.sh`
8) `cd ~/BOB_scripts/vps_scripts`
9) Install and sync all coin deamons you are going to use
10) `./start`
11) then shut down this VPS and make a copy of it X times for how many bobs you want to deploy.

## Installing Local Copy to your Linux Computer
This part of the guide will need updating. We should make a simple GUI for managing a while bunch of marketmakers with just a few clicks.
1) install git
2) `git clone https://github.com/blackjok3rtt/BOB_scripts.git`
3) `cd BOB_scripts/scripts`
4) edit the passprase file, its an array of passphrases for all your bobs.
5) edit the IP file, each line here matches the line of the passprases file.`
7) `./login.sh X` where X is the number of your VPS starting at 1.
8) when you are finished working in this VPS `./logout`

## Setting up your VPS
1) the userpass for this VPS is set on login you can use and scripts in the dexscipts folder.
2) you will need to edit them for your needs. Copy the whole folder of dexscripts and edit as required.

## Funding your bobs
Follow the guide in the README.md in the scripts folder.

