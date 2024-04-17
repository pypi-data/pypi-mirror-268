
'''

'''
import datetime

def start (csv_path):
	trend = []

	import csv
	with open (csv_path) as csv_file:
		csv_reader = csv.reader (csv_file, delimiter = ',')
		line_count = 0
		#for row in csv_reader:
		#	print (row)
			
		headers = next (csv_reader)
		headers = [ s.lower () for s in headers ]
		print ("headers:", headers)
		
		for row in csv_reader:
			trend.append (dict (zip (headers, row)))


	date_type = "string"

	'''
		2023-02[Feb]-09
	'''
	for line in trend:
		line ["unadjusted close"] = line ["adj close"]
		line ["close"] = float (line ["adj close"])
		del line ['adj close']
		
		'''
		
		'''
		if (date_type == "string"):
			line ["date string"] = line ["date"]
		else:
			parsed_date = line ["date"].split ("-")
			assert (len (parsed_date) == 3)
			line ["date string"] = datetime.datetime (
				year = int (parsed_date [0]), 
				month = int (parsed_date [1]), 
				day = int (parsed_date [2])
			)
		
		del line ['date']
		
		line ["open"] = float (line ["open"])
		line ["high"] = float (line ["high"])
		line ["low"] = float (line ["low"])
		

	#print (json.dumps (trend, indent = 4))
	
	return trend;