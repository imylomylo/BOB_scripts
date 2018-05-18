sudo apt-get update
sudo apt-get install git libcurl4-openssl-dev build-essential libnanomsg-dev cmake screen

git clone https://github.com/nanomsg/nanomsg.git
cd nanomsg
mkdir build
cd build
cmake ..
cmake --build .
sudo cmake --build . --target install
sudo ldconfig

cd ~
git clone https://github.com/jl777/SuperNET.git -b dev
cd SuperNET/iguana
./m_mm
cp marketmaker ~/BOB_scripts/vps_scripts/
