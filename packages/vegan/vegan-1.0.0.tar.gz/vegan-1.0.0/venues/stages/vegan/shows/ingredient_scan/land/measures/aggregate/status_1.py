
'''
	python3 insurance.py shows/ingredient_scan/land/measures/aggregate/status_1.py
'''


import vegan.mixes.insure.equality as equality	
	
import vegan.clouds.food_USDA.examples as USDA_examples	
import vegan.clouds.food_USDA.nature as food_USDA_nature

import vegan.shows.ingredient_scan.land.measures.aggregate as land_measures_aggregate
	
def check_1 ():
	walnuts_1882785 = food_USDA_nature.create (
		USDA_examples.retrieve ("branded/walnuts_1882785.JSON")
	)

	land = walnuts_1882785 ["essential nutrients"]
	land_measures_aggregate.calc (
		land = land
	)

	return;
	
checks = {
	'check 1': check_1
}