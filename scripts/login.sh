#!/bin/bash
source passphrase
userpass=$(curl -s --url "http://127.0.0.1:6650" --data "{\"userpass\":\"1d8b27b21efabcd96571cd56f91a40fb9aa4cc623d273c63bf9223dc6f8cd81f\",\"method\":\"passphrase\",\"passphrase\":\"$passphrase\",\"gui\":\"nogui\"}" | jq .userpass)
if [ $userpass != "" ]
  then
    echo "export userpass=$userpass" > userpass
    cp userpass dexscripts/
    echo "Login Sucessful"
  else
    echo "Failed to login"
fi

