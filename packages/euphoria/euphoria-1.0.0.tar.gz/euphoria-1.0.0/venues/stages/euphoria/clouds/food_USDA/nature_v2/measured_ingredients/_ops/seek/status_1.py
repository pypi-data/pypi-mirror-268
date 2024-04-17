
'''
	python3 status.proc.py clouds/food_USDA/nature_v2/measured_ingredients/_ops/seek/status_1.py
'''

import euphoria.clouds.food_USDA.deliveries.one.assertions.foundational as assertions_foundational
import euphoria.clouds.food_USDA.examples as USDA_examples	

import euphoria.clouds.food_USDA.nature_v2 as food_USDA_nature_v2
from euphoria.clouds.food_USDA.nature_v2.measured_ingredients._ops.seek import seek_measured_ingredient

import euphoria.mixes.insure.equalities as equalities

import json	


def check_1 ():
	walnuts_1882785 = USDA_examples.retrieve ("branded/walnuts_1882785.JSON")
	assertions_foundational.run (walnuts_1882785)
	
	measured_ingredients_list = food_USDA_nature_v2.create (
		walnuts_1882785,
		return_measured_ingredients_list = True
	)
	
	energy = seek_measured_ingredient ("energy", measured_ingredients_list)
	assert (type (energy) == dict)
	
	not_found = seek_measured_ingredient ("an ingredient not in the list", measured_ingredients_list)
	assert (not_found == None)

	
	print ("not_found", not_found)
	
checks = {
	'check 1': check_1
}