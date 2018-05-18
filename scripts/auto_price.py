#!/usr/bin/env python3
import requests
import json
import pprint
import sys
import os

# config area
mm_ip = '127.0.0.1'
mm_port = '6650'
# end of config area

#Define marketmaker URL
mm_url = 'http://' + mm_ip + ':' + mm_port

#read the userpass 
try:
	userpass = os.environ['userpass']
except:
	print("Error: userpass is not defined")
	sys.exit(0)
	
# configure pretty printer
pp = pprint.PrettyPrinter(width=41, compact=True)

# define function that posts json data to marketmaker
def post_rpc(url,payload):
    try:
        r = requests.post(url, data=json.dumps(payload))
        return(json.loads(r.text))
    except Exception as e:
        print("Couldn't connect to " + url, e)
        sys.exit(0)

#Get commandline arguments
COIN1=str(sys.argv[1])
xCOIN1=int(sys.argv[2])
COIN2=str(sys.argv[3])
xCOIN2=int(sys.argv[4])
spread=float(sys.argv[5])

#Calculate base/rel prices
pCOIN1 = round(xCOIN2 / xCOIN1, 8)
pCOIN2 = round(xCOIN1 / xCOIN2, 8)

#set spread
x = 1 - (spread / 2)
spCOIN1 = round(pCOIN1 * x, 8)
spCOIN2 = round(pCOIN2 * x, 8)

#print prices
print('1 ' + COIN1 + ' buys: ' + str(spCOIN2) + ' ' + COIN2)
print('1 ' + COIN2 + ' buys: ' + str(spCOIN1) + ' ' + COIN1)

#Define JSON for MM autoprice - base COIN1
autoprice_COIN1 = {
	"userpass" : userpass,
	"method" : "autoprice",
	"base" : COIN2,
	"rel" : COIN1,
	"fixed" : spCOIN2,
	"margin" :0.01
}
#Define JSON for MM autoprice - base COIN2
autoprice_COIN2 = {
	"userpass" : userpass,
	"method" : "autoprice",
	"base" : COIN1,
	"rel" : COIN2,
	"fixed" : spCOIN1,
	"margin" :0.01
}

#Send JSON payload base COIN1 to MM
response_autoprice_COIN1 = post_rpc(mm_url,autoprice_COIN1)
print('== response_autoprice_' + COIN1 + '==')
pp.pprint(response_autoprice_COIN1)

#Send JSON payload base COIN2 to MM
response_autoprice_COIN2 = post_rpc(mm_url,autoprice_COIN2)
print('== response_autoprice_' + COIN2 + '==')
pp.pprint(response_autoprice_COIN2)

autoprice_OOT = {
	"userpass" : userpass,
	"method" : "autoprice",
	"base" : "OOT",
	"rel" : "COQUI",
	"fixed" : "0.03",
	"margin" :0.01
}
#Send JSON payload base COIN2 to MM
response_autoprice_OOT = post_rpc(mm_url,autoprice_COIN2)
print('== response_autoprice_' + "OOT" + '==')
pp.pprint(response_autoprice_OOT)
