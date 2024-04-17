



'''
	description:
		This builds the essential nutrients land from 
		the measured ingredients.
'''

#
#	Essential Nutrients: land
#
'''
import euphoria.shows.ingredient_scan.land.add_measured_ingredient as add_measured_ingredient
import euphoria.shows.ingredient_scan.land.build as build_ingredients_land
import euphoria.shows.ingredient_scan.land.measures.sums as land_measures_sums
import euphoria.shows.ingredient_scan.land.calculate_portions as calculate_portions
import euphoria.shows.ingredient_scan.land.cultivate as cultivate_ingredient_scan_land	
	
#
#	Essential Nutrients: grove
#
import euphoria.shows.ingredient_scan.grove.seek as grove_seek
import euphoria.shows.ingredient_scan.grove.seek_count as seek_grove_count
import euphoria.shows.ingredient_scan.grove.has_uniters as has_uniters

#
#	Essential Nutrients: assertions
#
import euphoria.shows.ingredient_scan.assertions.one as ingredients_assertions_one
'''
	
import json	

from euphoria.shows_v2.treasure.nature.land import develop_land
	

def build_essential_nutrients_land (
	measured_ingredients = [],
	identity = {},
	records = 1
):	
	land = develop_land ()
	grove = land ["grove"]
	natures = land ["natures"]
		
	natures.append ({
		"amount": "1",
		"identity": identity
	})	
	
	
	#
	#	This constructs the:
	#	essential nutrients grove
	#
	for measured_ingredient in measured_ingredients:	
		if (records >= 1):
			if ("name" in measured_ingredient):
				print ("measured_ingredient:", measured_ingredient ['name'])
			else:
				print ("A name was not found in", measured_ingredient)
		


	return land;