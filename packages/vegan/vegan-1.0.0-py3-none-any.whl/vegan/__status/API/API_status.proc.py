




def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_directory = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_directory, path)))

add_paths_to_system ([
	'../../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath
import sys

import biotech

stage_name = "vegan"

this_directory = pathlib.Path (__file__).parent.resolve ()
venues = str (normpath (join (this_directory, "../../../../venues")))
this_stage = str (normpath (join (venues, f"stages/{ stage_name }")))


if (len (sys.argv) >= 2):
	glob_string = this_stage + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = this_stage + '/**/API_status_*.py'
	db_directory = normpath (join (this_directory, "db_API"))

#glob_string = venues + '/stages/**/API_status_*.py'


scan = biotech.start (
	glob_string = glob_string,
	simultaneous = True,
	module_paths = [
		normpath (join (venues, "stages")),
		normpath (join (venues, "stages_pip"))
	],
	relative_path = normpath (join (venues, f"stages/{ stage_name }")),
	
	db_directory = db_directory
)
