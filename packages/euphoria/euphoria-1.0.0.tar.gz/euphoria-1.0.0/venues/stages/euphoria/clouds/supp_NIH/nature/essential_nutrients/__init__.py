
'''
	import euphoria.clouds.supp_NIH.nature.ingredient_scan as calculate_ingredient_scan
	calculate_ingredient_scan.eloquently (
		measured_ingredients_grove
	)
'''

import euphoria.clouds.supp_NIH.nature.measured_ingredients.seek as seek

import euphoria.shows.ingredient_scan.assertions.one as ingredients_assertions_one	
import euphoria.shows.ingredient_scan.grove.has_uniters as has_uniters
import euphoria.shows.ingredient_scan.land.add_measured_ingredient as add_measured_ingredient
import euphoria.shows.ingredient_scan.land.build as build_ingredient_scan_land
import euphoria.shows.ingredient_scan.land.calculate_portions as calculate_portions
import euphoria.shows.ingredient_scan.land.measures.sums as land_measures_sums

import json

def eloquently (
	measured_ingredients_grove,
	identity
):
	ingredient_scan_land = build_ingredient_scan_land.eloquently ()
	ingredient_scan_grove = ingredient_scan_land ["grove"]
	ingredient_scan_natures = ingredient_scan_land ["natures"]
		
	ingredient_scan_natures.append ({
		"amount": "1",
		"identity": identity
	})	
	
	not_found = []
	
	
	'''
		This adds the measured ingredients to the grove.
	'''
	def for_each (
		measured_ingredient, 
		indent = 0, 
		parent_measured_ingredient = None
	):
		found = add_measured_ingredient.beautifully (
			#
			#	This is a reference to the land.
			#
			land = ingredient_scan_land,
			
			amount = 1,
			source = identity,
			measured_ingredient = measured_ingredient,
			
			return_False_if_not_found = True
		)
		if (not found):
			not_found.append (measured_ingredient ["name"])
		
		
		return False;

	seek.beautifully (
		measured_ingredients = measured_ingredients_grove,
		for_each = for_each
	)
	
	
	'''
		This adds the sums of the grove.
		
			This calculate the measure sums of the supp
			from the the measures of the supp ingredients.
	'''
	land_measures_sums.calc (
		land = ingredient_scan_land
	)
	
	'''
		The Portion Calculations
	'''
	calculate_portions.illustriously (
		land = ingredient_scan_land
	)
	
	'''
		Unity Check
	
		description:
			This makes sure that the story 2 and above "essentials",
			have a uniter that has "natures".
			
			That is make sure if "added, sugars" is listed,
			that "sugars, total" is listed.
		
		example:
			sugars, total	<- make sure that this exists, if "added sugars" is added.
				added, sugars
	'''
	has_uniters.check (ingredient_scan_grove)
	
	
	'''
		Assertions
	'''
	ingredients_assertions_one.sweetly (
		land = ingredient_scan_land
	)	
	
	
	#print ("These ingredients were not found:", not_found)

	return ingredient_scan_land