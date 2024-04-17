
'''
#
#	find name
#
import vegan.shows.ingredient_scan.DB.scan.seek as seek_nutrient
nutrient = seek_nutrient.presently (
	for_each = lambda essential : True if "thiamin" in essential ["names"] else False
)
'''

'''
#
#	find name
#
import vegan.shows.ingredient_scan.DB.scan.seek as seek_nutrient

ingredient = "ThiamIn"

def for_each (essential):
	for name in essential ["names"]:
		if (name.lower () == ingredient.lower ()):
			return True;
		
	return False

nutrient = seek_nutrient.presently (
	for_each = for_each
)
'''

'''
#
#	find region
#
import vegan.shows.ingredient_scan.DB.scan.seek as seek_nutrient
nutrient = seek_nutrient.presently (
	for_each = lambda essential : True if essential ["region"] == 1 else False
)
'''

import vegan.shows.ingredient_scan.DB.scan.list as ingredients_DB_list_scan

def for_each ():
	return False
	
def presently (
	for_each = for_each
):
	essentials = ingredients_DB_list_scan.retrieve ()
	for essential in essentials:
		if (for_each (essential)):
			return essential
	
	return None