# Bob_scripts
Scripts for funding and managing bobs.
The best way to do this is to have your marketmaker on a VPS and SSH tunnel to it like so: 

`nc -z localhost 7783 || ssh -f -N -L 7783:localhost:7783 user@vps; echo 'tunnel open'`

This first checks if a tunnel is already open if not it will open it. 

You need to set the parameters at the top of each script to point it at your marketmaker rpc port for the above SSH command it is 7783.
```
# config area
mm_ip = '127.0.0.1'
mm_port = '6650'
# end of config area
```

### Userpass
`userpass` must be set in the bash environment you run these scripts from. 

`export userpass=userpassofyouraccount`

### Set Auto Price-- Highest priced coin goes first
This script sets a pair of coins based on their price in BTC, I think someone can use an exchange API to pull the coins price in realtime every X minutes/hours to stop large arbs being possible due to price flutuations.

./autoscript COIN1 COIN1_PRICE COIN2 COIN2_PRICE SPREAD

Example:

`./auto_price.py KMD 40000 SNG 2450 0.05`

-------------------------------------------------
### Funding address's:

This script is very handy to fund bobs. make the Pairs (X) and (X)x1.2. The reason for not funding the x1.2 hard coded in, is so you can also fund alice with this for buying huge amounts of a coin, for a dICO etc. I found it best to have an address with the main funds you then fund all the bobs with. Just login to you makretmaker with another passprase and change userpass.

I suggest using UTXO pairs with an X value of 1, 10, 100, 1000 10,000 etc... Someone else might have better sizings since things have now chainged a bit since I made these.

./fundBob COIN ADDRESS 'number of UTXO pairs' UTXO-1 UTXO-2

Example

`./fundBob KMD RX8SinRsb1n9CMX68D8eQuuZLLqAJqU9Q9 50 10 12`
