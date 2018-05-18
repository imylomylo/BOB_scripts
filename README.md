# LP_scripts
Scripts for funding and managing LP's
The best way to do this is to have your marketmaker on a VPS and SSH tunnel to it like so: 


You need to set the parameters at the top of each script to point it at your marketmaker rpc port.
```
# config area
mm_ip = '127.0.0.1'
mm_port = '6650'
# end of config area
```

### set auto price-- Highest priced coin goes first

./autoscript KMD KMD_PRICE SNG SNG_PRICE SPREAD

Example:

`./auto_price.py KMD 40000 SNG 2450 0.05`

-------------------------------------------------
### Funding address's:

This script is very handy to fund bobs. make the Pairs (X) and (X)x1.2. The reason for not funding the x1.2 hard coded in, is so you can also fund alice with this for buying huge amounts of a coin, for a dICO etc.

I suggest using UTXO pairs with an X value of 1, 10, 100, 1000 10,000 etc... Someone else might have better sizings since things have now chainged a bit since I made these.

./fundLP COIN ADDRESS 'number of UTXO pairs' UTXO-1 UTXO-2

Example

`./fundLP KMD RX8SinRsb1n9CMX68D8eQuuZLLqAJqU9Q9 50 10 12`
