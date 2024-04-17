



'''
	share_price_current = 7.75

	option_strike_price = 5
	option_ask_price = 3.35

	import rollercoaster.treasures.options.multipliers as multipliers
	the_multipliers = multipliers.formulate_call (
		share_price_possibilities = [
			30,
			25,
			20,
			15,
			10,
			9,
			8.5,
			8,
			7,
			5,
			0
		],
		share_price_current = share_price_current,

		option_strike_price = option_strike_price,
		option_ask_price = option_ask_price
	)


	rich.print_json (data = the_multipliers)

	multipliers.print_report (the_multipliers)
'''

import numpy

'''

'''
def the_formula (
	share_price_possibility,
	option_ask_price,
	option_strike_price
):
	return (
		(share_price_possibility - option_strike_price) /
		option_ask_price
	)
	
from tabulate import tabulate
def print_report (object):
	print ("option_strike_price:", object ["option"] ["strike"])
	print ("option_ask_price:", object ["option"] ["ask"])
	
	the_multipliers = object ["multipliers"]
	
	data = []
	for multiplier in the_multipliers:
		data.append ([ 
			multiplier ["share_price"], 
			multiplier ["call"] ["multiplier"],
			multiplier ["share"] ["multiplier"]

		])
		
	table = tabulate (
		data, 
		headers = [ "share_price", "call multiplier", "share multiplier" ], 
		tablefmt="grid"
	)

	print (table)

def formulate_call (
	share_price_possibilities = [],
	share_price_current = "",
	
	option_ask_price = "",
	option_strike_price = ""
):
	multipliers = []
	for share_price_possibility in share_price_possibilities:
		break_even = option_strike_price + option_ask_price;
		
		if (break_even < share_price_possibility):			
			try:
				multiplier = the_formula (
					share_price_possibility,
					option_ask_price,
					option_strike_price
				)
			except:
				multiplier = "?"
		
		else:
			multiplier = 0
		
		multipliers.append ({
			"share_price": share_price_possibility,
			"call": {
				"multiplier percent": str (numpy.round (multiplier * 100, decimals = 3)) + "%",
				"multiplier": str (numpy.round (multiplier, decimals = 3)),
			},
			"share": {
				"multiplier": str (numpy.round (share_price_possibility / share_price_current, decimals = 3)), 
			},
			"stats": {
				"in the money if >": break_even,
				"price amount change": share_price_possibility - share_price_current,
				"price multiplier change": share_price_possibility / share_price_current,
				"price percentage change": str ((share_price_possibility / share_price_current) * 100) + "%"
			}
		})
		

	return {
		"option": {
			"strike": option_strike_price,
			"ask": option_ask_price
		},
		"multipliers": multipliers
	}