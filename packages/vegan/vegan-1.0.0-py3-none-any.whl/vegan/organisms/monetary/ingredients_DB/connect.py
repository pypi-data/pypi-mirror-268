
'''
	import vegan.monetary.ingredients_DB.connect as connect_to_ingredient
	ingredients_DB = connect_to_ingredient.DB (
		vegan_essence = vegan_essence
	)
'''

from vegan._essence import receive_monetary_URL

import pymongo

def DB (
	vegan_essence = {}
):
	# URL = vegan_essence ["monetary"] ["URL"]
	
	monetary_URL = receive_monetary_URL (
		vegan_essence = vegan_essence
	)
	
	DB_name = vegan_essence ["monetary"] ["DB_name"]

	mongo_connection = pymongo.MongoClient (monetary_URL)
	DB = mongo_connection [ DB_name ]

	return DB