
'''
	import euphoria.monetary.ingredients_DB.connect as connect_to_ingredient
	ingredients_DB = connect_to_ingredient.DB (
		euphoria_essence = euphoria_essence
	)
'''

from euphoria._essence import receive_monetary_URL

import pymongo

def DB (
	euphoria_essence = {}
):
	# URL = euphoria_essence ["monetary"] ["URL"]
	
	monetary_URL = receive_monetary_URL (
		euphoria_essence = euphoria_essence
	)
	
	DB_name = euphoria_essence ["monetary"] ["DB_name"]

	mongo_connection = pymongo.MongoClient (monetary_URL)
	DB = mongo_connection [ DB_name ]

	return DB