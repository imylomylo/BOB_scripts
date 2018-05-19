#!/usr/bin/env python3
import requests
import json
import pprint
import sys
import os
import random

# config area
mm_ip = '127.0.0.1'
mm_port = '7783'
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
    
#Define function to create outputs array    
def create_outputs(address,amount,low,high):
	outputs = []
	for i in range(amount):
		new_output = {address : low}
		outputs.append(new_output)
		new_output = {address : high}
		outputs.append(new_output)
	return(outputs) 

#Get command line inputs
i_coin = str(sys.argv[1])
i_address = str(sys.argv[2])
i_amount = int(sys.argv[3])
i_low = float(sys.argv[4])
i_high = float(sys.argv[5])

#Define outputs array
TXoutput = create_outputs(i_address,i_amount,i_low,i_high)

#Define Withdraw API JSON
withdraw = {
	"userpass" : userpass,
	"method" : "withdraw",
	"coin" : i_coin,
	"outputs" : TXoutput
}

#Send payload withdraw API
response_withdraw = post_rpc(mm_url,withdraw)
print('== response_withdraw ==')
pp.pprint(response_withdraw)

#Extract rawtx from response
rawtx = response_withdraw['hex']

#Define SendRaw Transaction
rawtx_send = {
	"userpass" : userpass,
	"method" : "sendrawtransaction",
	"coin" : i_coin ,
	"signedtx" : str(rawtx)
}

print(rawtx_send)

#Send JSON payload base COQUI to MM
response_sendrawtx = post_rpc(mm_url,rawtx_send)
print('== response_sendrawtx ==')
pp.pprint(response_sendrawtx)
