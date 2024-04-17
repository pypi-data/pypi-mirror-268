




******

Bravo!  You have received a Medical Diploma from   
the Orbital Convergence University International Air and Water Embassy of the Tangerine Planet.  

You are now officially certified to include this module in your practice.

******


# ramps_galactic

---

## description

		
		
---		
		
## install
```
pip install ramps_galactic
```

--

## usage
```
"date string": "",
"high": "",
"low": "",
"open": "",
"close": ""
```


```
from datetime import datetime
import json
import pprint

import pandas
import rich	

import ramps_galactic
import ramps_galactic.victory_multiplier.purchase_treasure_at_inclines as purchase_treasure_at_inclines_VM	
import ramps_galactic.victory_multiplier.purchase_treasure_over_span as purchase_treasure_over_span_VM
import ramps_galactic.example_data.read as read_example_data

trend = read_example_data.start ("yahoo-finance--BTC-USD.CSV")	
trend_DF = pandas.DataFrame (trend)	

enhanced_trend_DF = ramps_galactic.calc (
	trend_DF,
	period = 14,
	multiplier = 2
)
enhanced_list = enhanced_trend_DF.to_dict ('records')


'''
	This calculates the multipliers
'''
victory_multiplier_if_riding = purchase_treasure_at_inclines_VM.calc (
	enhanced_trend_DF,
	include_last_change = False
)

rich.print_json (data = victory_multiplier_if_riding ["relevant"])	

victory_multiplier_if_holding = purchase_treasure_over_span_VM.calc (enhanced_trend_DF)
print (
	"The multiplier if holding over the entire interval:",
	victory_multiplier_if_holding
)
print (
	"The multiplier if trading the ramp:", 
	victory_multiplier_if_riding ["treasure purchase victory multiplier"]
)

rich.print_json (data = victory_multiplier_if_riding)

current_trend = victory_multiplier_if_riding ["current trend"]
print ('current trend:', current_trend)

'''
	If you would like to open the chart:
'''
if (True):
	ramps_galactic.chart_the_data (
		enhanced_trend_DF,
		victory_multiplier_if_riding
	)
```