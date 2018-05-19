# Bob_scripts
Scripts for funding and managing bobs.
This repo is designed to manage a number of bobs that do the same thing. BarterDEX works much better is there are lots of bobs. For this you need native coind's.

To use the python scripts here you need to set the config area at the top of each script. By default the Price script is set for VPS marketmaker and the Fund script is set for your local marketmaker.

```
# config area
mm_ip = '127.0.0.1'
mm_port = '7783'
# end of config area
```

### Set Auto Price-- Highest priced coin goes first
This script sets a pair of coins based on their price in BTC, I think someone can use an exchange API to pull the coins price in realtime every X minutes/hours to stop large arbs being possible due to price flutuations. This is for coins not listed on CMC. For that you can use autoprice API. There are some examples in the dexscripts folder.

`source userpass;./autoprice.py COIN1 COIN1_PRICE COIN2 COIN2_PRICE SPREAD`

Example:

`source userpass;./auto_price.py KMD 40000 SNG 2450 0.05`

-------------------------------------------------
### Funding address's:

This script is very handy to fund bobs. make the Pairs (X) and (X)x1.2. The reason for not funding the x1.2 hard coded in, is so you can also fund alice with this for buying huge amounts of a coin, for a dICO etc. I found it best to have an address with the main funds you then fund all the bobs with. I use my local marketmaker with just electrum to fund without any issues. This is why its config area is using port 7783.

Fund large UTXO's as the change from each purchase will last longer before becoming dust and slowing down your bob.

`source userpass;./fundbob.py COIN ADDRESS 'number of UTXO pairs' UTXO-1 UTXO-2`

Example

`source userpass;./fundbob.py KMD RX8SinRsb1n9CMX68D8eQuuZLLqAJqU9Q9 50 10 12`
