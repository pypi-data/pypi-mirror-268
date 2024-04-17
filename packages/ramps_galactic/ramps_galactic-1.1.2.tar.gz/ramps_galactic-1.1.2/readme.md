




******

Bravo!  You have received a Medical Diploma from   
the Orbital Convergence University International Air and Water Embassy of the Tangerine Planet.  

You are now officially certified to include this module in your practice.

******


# ramps_majestic

---

## description

		
		
---		
		
## install
```
pip install ramps_majestic
```

--

## usage
```
from datetime import datetime
import json
import pprint

import pandas
import rich	

import ramps_majestic
import ramps_majestic.victory_multiplier.purchase_treasure_at_inclines as purchase_treasure_at_inclines_VM	
import ramps_majestic.victory_multiplier.purchase_treasure_over_span as purchase_treasure_over_span_VM
import ramps_majestic.example_data.read as read_example_data

trend = read_example_data.start ("yahoo-finance--BTC-USD.CSV")	
trend_DF = pandas.DataFrame (trend)	

enhanced_trend_DF = ramps_majestic.calc (
	trend_DF,
	period = 14,
	multiplier = 3
)
enhanced_list = enhanced_trend_DF.to_dict ('records')


'''
	This calculates the multipliers
'''
treasure_at_inclines_VM = purchase_treasure_at_inclines_VM.calc (
	enhanced_trend_DF,
	include_last_change = True
)

rich.print_json (data = treasure_at_inclines_VM ["relevant"])	

open_price_at_spans_VM = purchase_treasure_over_span_VM.calc (enhanced_trend_DF)
print ("open_price_at_spans_VM:", open_price_at_spans_VM)
print ("treasure_at_inclines_VM:", treasure_at_inclines_VM ["treasure purchase victory multiplier"])


ramps_majestic.chart_the_data (
	enhanced_trend_DF,
	treasure_at_inclines_VM
)
```