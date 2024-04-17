

'''
	import ramps_galactic.victory_multiplier.purchase_treasure_over_span as purchase_treasure_over_span_VM
	open_price_at_spans_VM = purchase_treasure_over_span_VM.calc (DF)
'''

def calc (DF):
	return float (
		DF ["open"].iloc [-1] / 
		DF ["open"].iloc [0]
	)	