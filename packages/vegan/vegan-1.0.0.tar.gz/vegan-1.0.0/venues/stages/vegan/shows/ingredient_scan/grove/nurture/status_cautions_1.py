


'''
	python3 insurance.py shows/ingredient_scan/grove/nurture/status_cautions_1.py
'''


import vegan.shows.ingredient_scan.grove.nurture as grove_nurture
import vegan.shows.ingredient_scan.grove.seek as grove_seek
import vegan.shows.ingredient_scan.grove.print as print_grove

import json

def check_1 ():
	'''
	import vegan.shows.ingredient_scan.DB.path as DB_paths
	import vegan.shows.ingredient_scan.DB.access as access
	cautions_DB_list = access.DB (
		path = DB_paths.find (DB = "cautions")
	)
	'''
	
	import vegan.shows.ingredient_scan.DB.path as DB_paths
	import vegan.shows.ingredient_scan.DB.access as access
	cautions_DB = access.DB (
		path = DB_paths.find (DB = "cautions")
	)

	import vegan.shows.ingredient_scan.grove.nurture as grove_nurture
	grove = grove_nurture.beautifully (
		ingredients_DB = cautions_DB
	)
	
	print_grove.beautifully (
		grove
	)
	
	def guarantee_ingredient (name):
		ingredient = grove_seek.beautifully (
			grove = grove,
			for_each = lambda entry : True if name in entry ["info"] ["names"] else False
		)
		assert (type (ingredient) == dict), ingredient
		assert (name in ingredient ["info"] ["names"])
		
		print ("ingredient:", ingredient)
		
	guarantee_ingredient (
		name = "trans fat"
	)
	
checks = {
	'check 1': check_1
}