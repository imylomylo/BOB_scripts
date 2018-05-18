#!/bin/bash
cd ~/komodo
git pull
make -j$(nproc)
