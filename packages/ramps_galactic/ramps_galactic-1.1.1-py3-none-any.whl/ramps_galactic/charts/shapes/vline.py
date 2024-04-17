

'''
	import ramps_galactic.charts.shapes.vline as vline_shapes
	vline_shapes.show (
		figure,
		DF = DF,
		x = ''
	)
'''

'''
	vertical_line_date = pandas.to_datetime('2023-06-13')
	chart.add_shape (
		type='line',
		x0=vertical_line_date,
		x1=vertical_line_date,
		y0=0,
		y1=20,
		line=dict(color='red', width=2, dash='dash')
	)
'''

import pandas

def show (
	figure,
	DF = None,
	x = None
):	

	vertical_line_date = pandas.to_datetime(x)
	figure.add_shape (
		type = 'line',
		x0 = vertical_line_date,
		x1 = vertical_line_date,
		y0 = DF ["high"].max (),
		y1 = 0,
		line = dict(color='red', width=2, dash='dash')
	)

	return;