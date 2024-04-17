
'''
	import apoplast.monetary.ingredients_DB.connect as connect_to_ingredient
	ingredients_DB = connect_to_ingredient.DB (
		apoplast_essence = apoplast_essence
	)
'''

from apoplast._essence import receive_monetary_URL

import pymongo

def DB (
	apoplast_essence = {}
):
	# URL = apoplast_essence ["monetary"] ["URL"]
	
	monetary_URL = receive_monetary_URL (
		apoplast_essence = apoplast_essence
	)
	
	DB_name = apoplast_essence ["monetary"] ["DB_name"]

	mongo_connection = pymongo.MongoClient (monetary_URL)
	DB = mongo_connection [ DB_name ]

	return DB