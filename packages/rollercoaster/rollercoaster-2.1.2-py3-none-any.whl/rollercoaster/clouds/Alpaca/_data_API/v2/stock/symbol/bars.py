
'''
	import rollercoaster.clouds.Alpaca._data_API.v2.stock.symbol.bars as Alpaca_bars
	spans = Alpaca_bars.retrieve (
		symbol = "VANI",
		params = {},
		headers = {
			"APCA-API-KEY-ID": "",
			"APCA-API-SECRET-KEY": ""
		}
	)
'''

import json
import requests

from pydash import objects as pydash_objects


def retrieve (
	symbol = '',
	headers = {},
	params = {}
):
	URL = f'https://data.alpaca.markets/v2/stocks/{symbol}/bars'
	
	merged_headers = pydash_objects.merge ({
		"accept": "application/json"
	}, headers)
	
	response = requests.get (
		URL,
		params = params,
		headers = headers
	)

	assert (response.status_code == 200), [
		response.status_code,
		response.text
	]

	response_text = response.text;
	response_JSON = json.loads (response_text)
	
	return {
		"JSON": response_JSON
	}