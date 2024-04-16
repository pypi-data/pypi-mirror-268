




def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../stages',
	'../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath
import sys

import body_scan

this_structure_name = "shares"

this_folder = pathlib.Path (__file__).parent.resolve ()
lands = str (normpath (join (this_folder, "../../../../venues")))

this_structure = str (normpath (join (lands, "stages", this_structure_name)))

status_assurances_path = str (normpath (join (this_folder, "..")))


if (len (sys.argv) >= 2):
	glob_string = status_assurances_path + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = status_assurances_path + '/**/status_*.py'
	db_directory = normpath (join (this_folder, "DB"))

print ("glob string:", glob_string)


scan = body_scan.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (lands, "stages")),
		normpath (join (lands, "stages_pip"))
	],
	relative_path = status_assurances_path
)
