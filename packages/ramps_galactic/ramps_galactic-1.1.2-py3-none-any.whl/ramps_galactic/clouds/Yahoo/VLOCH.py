


'''
	import ramps_galactic.clouds.Yahoo.VLOCH as Yahoo_VLOCH
	from datetime import datetime, timedelta
	
	end_date = datetime.today()
	start_date = end_date - timedelta(days=100)
	
	trend_DF = Yahoo_VLOCH.retrieve ({
		"symbol": "OTLY",
		
		"span": [
			start_date,
			end_date
		],
		
		"quant": "1h"
	})
'''

from datetime import datetime, timedelta

import yfinance as yf

def retrieve (packet):
	symbol = packet ["symbol"]
	span = packet ["span"]
	quant = packet ["quant"]
	
	trend_DF = yf.download(
		"OTLY", 
		start = span [0], 
		end = span [1], 
		interval = quant
	)
	
	trend_DF.rename (
		columns = {
			'Open': 'open', 
			'Close': 'unadjusted close',
			'Adj Close': 'close',
			
			'High': 'high',
			'Low': 'low',
			
			'Volume': 'volume'
			
		},
		inplace = True
	)
	
	
	trend_DF ['date string'] = trend_DF.index
	#trend_DF ['date string'] = trend_DF ['date string'].dt.tz_localize('UTC')
	trend_DF ['date string'] = trend_DF ['date string'].dt.strftime('%Y-%m-%d %H:%M')
	
	#print (trend_DF.columns.tolist ())
	#print (trend_DF)
	
	trend_DF = trend_DF.reset_index(drop=True)
	#trend_DF ['date string'] = trend_DF ['date string'].dt.strftime ('%Y-%m-%d')
	
	return trend_DF;