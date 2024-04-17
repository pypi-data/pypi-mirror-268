

'''
	caution, not checked.

		import vegan.shows.ingredient_scan.DB.access as access
		import vegan.shows.ingredient_scan.DB.sculpt.essential.adapt_every as adapt_every_essential_nutrient
	
		def for_each (essential):
			return essential

		adapt_every_essential_nutrient.eloquently (
			essentials_DB = access.DB (),
			for_each = for_each
		)
'''

import vegan.shows.ingredient_scan.DB.access as access

import vegan.shows.ingredient_scan.DB.scan.seek_next_region as seek_next_region
import vegan.shows.ingredient_scan.DB.scan.seek as seek_nutrient
import vegan.shows.ingredient_scan.DB.scan.list as ingredients_DB_list_scan

from tinydb import TinyDB, Query

import json

def for_each ():
	return;

def eloquently (
	essentials_DB = access.DB (),
	for_each = for_each
):
	
	import vegan.shows.ingredient_scan.DB.access as access
	essentials = ingredients_DB_list_scan.retrieve (
		essentials_DB = access.DB ()
	)

	for essential in essentials:
		essential = for_each (essential)
		region = essential ["region"]

		updated = essentials_DB.update (
			essential, 
			Query ().region == region
		)
		
		#print ("updated:", updated)
	

		