#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script shows the current bitcoin rate in Euro. 

from UHScroll import *
import cbpro
import datetime

public_client = cbpro.PublicClient()

print '----------------------------'
data_btc = public_client.get_product_ticker(product_id='BTC-EUR')
btc_price = data_btc['price']
btc_time = data_btc['time']

btc_new_price = str(btc_price).split('.')[0]
btc_old_price_temp = open(".btc", "r")
btc_old_price = btc_old_price_temp.readline()

print 'Bitcoinkurs von Coinbase Pro'
print 'Neuer Preis: ' + btc_new_price + ' Euro'
print 'Alter Preis: '+ btc_old_price + ' Euro'
print '----------------------------'


if str(btc_new_price) > str(btc_old_price):
    unicorn_scroll('~bcoin','white',120,0.095)
    unicorn_scroll(btc_new_price+'~euros'+' + + + '+btc_new_price+'~euros','green',180,0.12)
elif str(btc_new_price) < str(btc_old_price):
    unicorn_scroll('~bcoin','white',180,0.12)
    unicorn_scroll(btc_new_price+'~euros'+' + + + '+btc_new_price+'~euros','red',120,0.095)
else:
    unicorn_scroll('~bcoin','white',120,0.095)
    unicorn_scroll(btc_new_price+'~euros'+' + + + '+btc_new_price+'~euros','yellow',120,0.095)

file = open(".btc","w")
file.write(btc_new_price)
file.close() 
