

'''
	mongo connection strings
		
		DB: vegan
			
			collection: 
				cautionary_ingredients
				essential_nutrients
'''


import pathlib
from os.path import dirname, join, normpath
import sys
def add_paths_to_system (paths):
	this_directory = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_directory, path)))
	

add_paths_to_system ([
	'../../../../stages',
	'../../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath
import sys
import biotech

'''
#import vegan.monetary.ingredients.DB.open as ingredient_DB
mongo_process = ingredient_DB.open (
	vegan_essence = vegan_essence
)
'''

name = "vegan"
this_directory = pathlib.Path (__file__).parent.resolve ()
venues = str (normpath (join (this_directory, "../../../../../venues")))
this_stage = str (normpath (join (venues, f"stages/{ name }")))

if (len (sys.argv) >= 2):
	glob_string = this_stage + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = this_stage + '/**/status_*.py'
	db_directory = normpath (join (this_directory, "DB"))

print ("glob string:", glob_string)

scan = biotech.start (
	glob_string = glob_string,
	
	simultaneous = True,
	simultaneous_capacity = 10,
	
	time_limit = 10,
	
	module_paths = [
		normpath (join (venues, "stages")),
		normpath (join (venues, "stages_pip"))
	],
	relative_path = this_stage,
	
	db_directory = db_directory,
	
	aggregation_format = 2
)



