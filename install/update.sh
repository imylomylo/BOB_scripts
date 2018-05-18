/#!/bin/bash
cd ~/SuperNET/iguana
git checkout dev
git pull
./m_mm
cp marketmaker ~/BOB_scripts/vps_scripts
