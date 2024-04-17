



'''
	based on:
		https://stackoverflow.com/questions/44935269/supertendency-code-using-pandas-python
'''


from ._clique import clique


'''
	pivot indicates a band change.
	
	The place 1 place after the pivot
	is where the purchase or sale event
	can occur at the open price.
	
		"galactic incline": "yes",
		"galactic decline": "no",
'''

'''
	import ramps_galactic
	enhanced_tendency_DF = galactic.calc ([{
		"high": "",
		"low": "",
		"open": "",
		"close": ""
	}])	
'''



from ramps_galactic.tendencies.galactic import calc


'''
	This charts the data
'''
import rich

import ramps_galactic
import ramps_galactic.victory_multiplier.purchase_treasure_at_inclines as purchase_treasure_at_inclines_VM	
import ramps_galactic.victory_multiplier.purchase_treasure_over_span as purchase_treasure_over_span_VM

import ramps_galactic.furniture.CSV.read as read_CSV

import ramps_galactic.charts.VLOCH as VLOCH
import ramps_galactic.charts.galactic_line as galactic_line
import ramps_galactic.charts.shapes.vline as vline_shape	
import ramps_galactic.charts.annotations.vline as vline_annotation
	
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from plotly.subplots import make_subplots	
import plotly.graph_objects as go	
#import plotly.graph_objs as go

def chart_the_data (
	enhanced_trend_DF = None,
	treasure_at_inclines_VM = None
):
	
	chart = VLOCH.show (
		DF = enhanced_trend_DF
	)
	
	galactic_line.attach (
		chart = chart,
		DF = enhanced_trend_DF
	)	
	
	relevant = treasure_at_inclines_VM ["relevant"]
	for place in relevant:
		multiplier = "()"
		if (type (place ["change"]) == float):
			multiplier = "(" + str (round (place ["aggregate change"], 3)) + ")";
		
		open = place ["open"]
	
		vline_shape.show (
			chart,
			DF = enhanced_trend_DF,
			x = place ["date string"]
		)
		vline_annotation.show (
			chart,
			DF = enhanced_trend_DF,
			x = place ["date string"],
			
			text = f"{ multiplier }"
		)

	#rich.print_json (data = treasure_at_inclines_VM ["relevant"])
	
	columns = list (relevant[0].keys())

	
	chart.append_trace ( 
		go.Table (
			header = dict(values=columns),
			cells = dict(values=list(zip(*[data.values() for data in relevant])))
		),
		row = 2,
		col = 1
	)
	
	
	#----
	#
	#
	#
	app = dash.Dash(__name__)
	app.layout = html.Div(
		style={'width': '100vw', 'height': '100vh'},
		children=[
			dcc.Graph(
				id='plot',
				figure=chart,
				style={'width': '100%', 'height': '100%'}
			)
		]
	)
	app.run_server(debug=True, port=5000, host = '0.0.0.0')
