# LP_scripts
Scripts for funding and managing LP's

###set auto price-- Highest priced coin goes first

./autoscript KMD KMD_PRICE SNG SNG_PRICE SPREAD

Example:

`./auto_price.py KMD 40000 SNG 2450 0.05`

-------------------------------------------------
###Funding address's:

./fundLP COIN ADDRESS 'number of UTXO pairs' UTXO-1 UTXO-2

Example

`./fundLP KMD RX8SinRsb1n9CMX68D8eQuuZLLqAJqU9Q9 50 0.1 0.7`
