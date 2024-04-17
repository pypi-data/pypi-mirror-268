




def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_directory_path = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_directory_path, path)))

add_paths_to_system ([
	'../../../stages',
	'../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath
import sys

import factory_farm

name = "ramps_galactic"

this_directory_path = pathlib.Path (__file__).parent.resolve ()
venues_path = str (normpath (join (this_directory_path, "../../../../venues")))
ramps_galactic = str (normpath (join (venues_path, "stages", name)))

status_assurances_path = str (normpath (join (this_directory_path, "..")))

if (len (sys.argv) >= 2):
	glob_string = status_assurances_path + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = status_assurances_path + '/**/status_*.py'
	db_directory = normpath (join (this_directory_path, "DB"))

print ("glob string:", glob_string)


scan = factory_farm.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (venues_path, "stages")),
		normpath (join (venues_path, "stages_pip"))
	],
	relative_path = status_assurances_path,
	
	db_directory = db_directory
)
