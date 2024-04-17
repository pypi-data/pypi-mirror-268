

'''
	import ramps_galactic.charts.annotations.vline as vline_annotation
	vline_annotation.show (
		figure,
		DF = DF
	)
'''

'''
	#
	#	https://plotly.com/python/horizontal-vertical-shapes/
	#

	import plotly.express as px

	df = px.data.stocks(indexed=True)
	fig = px.line(df)
	fig.add_hline(y=1, line_dash="dot",
				  annotation_text="Jan 1, 2018 baseline", 
				  annotation_position="bottom right")
	fig.add_vrect(x0="2018-09-24", x1="2018-12-18", 
				  annotation_text="decline", annotation_position="top left",
				  fillcolor="green", opacity=0.25, line_width=0)
	fig.show()
'''

import pandas

def show (
	figure,
	DF = None,
	x = None,
	text = "annotation"
):	

	#
	'''
	figure.add_vline (
		x = pandas.to_datetime (x), 
		
		#xref = 'date string',
		line_dash= "dot",
		annotation_text = "A text annotation", 
		annotation_position = "bottom right"
	)
	'''

	figure.add_annotation(
		x = pandas.to_datetime (x), 
		y = DF['high'].max(),
		text = text, 
		showarrow = True, 
		arrowhead = 2, 
		arrowcolor = "red", 
		arrowsize = 1.5
	)

	return;