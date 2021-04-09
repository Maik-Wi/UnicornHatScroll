#!/usr/bin/env python
# -*- coding: utf-8 -*-

from UHScroll import *
import cbpro
import datetime

public_client = cbpro.PublicClient()

def coinbase():
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
	
	if str(btc_new_price) > str(btc_old_price):
	    unicorn_scroll(btc_new_price+'~euros','green',255,0.12)
	elif str(btc_new_price) < str(btc_old_price):
	    unicorn_scroll(btc_new_price+'~euros','red',180,0.12)
	else:
	    unicorn_scroll(btc_new_price+'~euros','yellow',230,0.12)
	
	file = open(".btc","w")
	file.write(btc_new_price)
	file.close()

while True:
	coinbase()
