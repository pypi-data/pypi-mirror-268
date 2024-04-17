
'''
	import ramps_galactic.charts.galactic_line as galactic_line
	galactic_line.attach (
		chart = chart,
		DF = enhanced_trend_DF
	)	
'''

import plotly.graph_objects as GO
def attach (
	chart, 
	DF, 
	line_name = "galactic line", 
	color = "purple"
):
	chart.add_trace (
		GO.Scatter (
			x = DF ['date string'], 
			y = DF [ line_name ], 
			line = dict (
				color = color, 
				width = 3
			)
		),
		row = 1,
		col = 1
	)