



def calc (
	DF,
	
	period = 14,
	multiplier = 3
):
	DF ['TR 1'] = abs (DF ["high"] - DF ["low"])
	DF ['TR 2'] = abs (DF ["high"] - DF ["close"].shift (1))
	DF ['TR 3'] = abs (DF ["low"]- DF ["close"].shift (1))
	DF ["TR"] = round (DF [[ 'TR 1', 'TR 2', 'TR 3' ]].max (axis = 1), 2)
	
	DF ["ATR"] = 0.00
	
	'''
		Basic and Final
	
		UB & LB:
			upper band and lower band?
	'''
	DF ['BUB'] = 0.00
	DF ["BLB"] = 0.00
	DF ["FUB"] = 0.00
	DF ["FLB"] = 0.00
	
	DF ["galactic line"] = 0.00
	
	# Calculating ATR 
	for i, row in DF.iterrows ():
		if i == 0:
			DF.loc [ i, 'ATR' ] = 0.00 
			#DF['ATR'].iat[0]
		else:
			DF.loc [ i, 'ATR'] = ((DF.loc[i-1,'ATR'] * (period - 1))+DF.loc[i,'TR'])/ period


	'''
		# Calculate Supertendency
		upper_band = (high + low) / 2 + multiplier * atr
		lower_band = (high + low) / 2 - multiplier * atr
	'''
	'''
		round to 2 decimal places..
	'''
	DF ['BUB'] = round (
		((DF ["high"] + DF ["low"]) / 2) + (multiplier * DF ["ATR"]),
		2
	)
	DF ['BLB'] = round (
		((DF ["high"] + DF ["low"]) / 2) - (multiplier * DF ["ATR"]),
		
		2
	)



	'''
		https://pandas.pyDF.org/pandas-docs/stable/reference/api/pandas.DFFrame.loc.html
	'''
	for i, row in DF.iterrows ():
		if i == 0:
			DF.loc [ i, "FUB"] = 0.00
		else:
			if (
				DF.loc [ i, "BUB" ] < DF.loc [ i - 1, "FUB" ]
			) | (
				DF.loc [ i - 1, "close" ] > DF.loc [ i - 1, "FUB" ]
			):
				DF.loc [ i, "FUB" ] = DF.loc[i,"BUB"]
			
			else:
				DF.loc [ i, "FUB" ] = DF.loc [ i - 1, "FUB" ]


	'''
	
	'''
	for i, row in DF.iterrows ():
		if i == 0:
			DF.loc [ i, "FLB" ]=0.00
		else:
			if (DF.loc[i,"BLB"]>DF.loc[i-1,"FLB"])|(DF.loc[i-1,"close"]<DF.loc[i-1,"FLB"]):
				DF.loc[i,"FLB"]=DF.loc[i,"BLB"]
			else:
				DF.loc[i,"FLB"]=DF.loc[i-1,"FLB"]

	'''
	
	'''
	for i, row in DF.iterrows ():
		if i == 0:
			DF.loc [ i, "galactic line" ] = 0.00
			
		elif (
			DF.loc[i-1,"galactic line"] == DF.loc[i-1,"FUB"]
		) & (
			DF.loc[i,"close"]<=DF.loc[i,"FUB"]
		):
			DF.loc[i,"galactic line"]=DF.loc[i,"FUB"]
		
		elif (
			DF.loc [i-1,"galactic line"] == DF.loc[i-1,"FUB"]
		) & (
			DF.loc [i,"close"] > DF.loc [ i, "FUB" ]
		):
			DF.loc[i,"galactic line"]=DF.loc[i,"FLB"]
		
		elif (
			DF.loc[i-1,"galactic line"]==DF.loc[i-1,"FLB"]
		) & (
			DF.loc[i,"close"] >= DF.loc[i,"FLB"]
		):
			DF.loc[i,"galactic line"]=DF.loc[i,"FLB"]
		
		elif (
			DF.loc [i-1,"galactic line"] == DF.loc [i-1,"FLB"]
		) & (
			DF.loc[i,"close"] < DF.loc[i,"FLB"]
		):
			DF.loc[i,"galactic line"] = DF.loc[i,"FUB"]


	
	

	'''
		This figures out the indicators
	'''
	pivot = "NA"
	for i, row in DF.iterrows ():	
		if (pivot == "yes"):
			pivot = "no"
	
		if i == 0:
			DF ["galactic estimate"] = "NA_move"
			tendency = "NA_move"
			
			if (tendency != "NA_move"):
				pivot = "yes"
			
		elif (DF.loc [ i, "galactic line" ] < DF.loc [ i, "close" ]):
			DF.loc [ i, "galactic estimate" ] = "incline_move"
			
			if (tendency != "incline_move"):
				pivot = "yes"
			
			tendency = "incline_move"
			
			
		else:
			DF.loc [ i, "galactic estimate" ] = "decline_move"
			
			if (tendency != "decline_move"):
				pivot = "yes"
			
			tendency = "decline_move"
		
		DF.loc [ i, "pivot" ] = pivot
		
		
	
	'''
	
	'''
	multiplier = 1;
	fee = 0
	estimate = "NA"
	pivot = "NA"
	quantity = 0;		
	for i, row in DF.iterrows ():
		pivot = DF.loc [ i, "pivot" ]
		estimate = DF.loc [ i, "galactic estimate" ]
		
		
		DF.loc [ i, "galactic step multiplier" ] = multiplier
		DF.loc [ i, "galactic incline" ] = "no"
		DF.loc [ i, "galactic decline" ] = "no"
	
		#print (estimate, pivot, DF.loc [ i, "open" ], multiplier)
	
		if (estimate == "incline_move"):
			if (DF.loc [ i - 1, "pivot" ] == "yes"):
				DF.loc [ i, "galactic incline" ] = "yes"
			
			if (pivot != "yes"):	
				DF.loc [ i, "quantity" ] = "1"
				quantity = "1"
				DF.loc [ i, "galactic step multiplier" ] = (
					DF.loc [ i, "open" ] / 
					DF.loc [ i - 1, "open" ]
				)
				
			else:
				DF.loc [ i, "quantity" ] = "0"
				quantity = "0"

		
		elif (estimate == "decline_move"):
			DF.loc [ i, "quantity" ] = "1"
			quantity = "1"
			
			if (DF.loc [ i - 1, "pivot" ] == "yes"):
				DF.loc [ i, "galactic decline" ] = "yes"
	
	'''
		aggregate multiplier
	'''
	ramp_multiplier = 1;
	for i, row in DF.iterrows ():
		ramp_multiplier = ramp_multiplier * DF.loc [ i, "galactic step multiplier" ]
	
		DF.loc [ i, "galactic ramp multiplier" ] = ramp_multiplier
			
	DF = DF.drop (columns = [
		'TR 1', 'TR 2', 'TR 3',
		'TR',
		'ATR',
		"BUB", "BLB", "FUB", "FLB"
	])		
			
	return DF;