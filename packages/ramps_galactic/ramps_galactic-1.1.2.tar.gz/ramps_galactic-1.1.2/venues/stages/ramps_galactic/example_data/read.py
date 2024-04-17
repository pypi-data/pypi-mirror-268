
import ramps_galactic.furniture.CSV.read as read_CSV

def relative_path (path):
	import pathlib
	from os.path import dirname, join, normpath
	import sys

	this_directory_path = pathlib.Path (__file__).parent.resolve ()	
	return str (normpath (join (this_directory_path, path)))

def start (name):
	return read_CSV.start (relative_path (name))