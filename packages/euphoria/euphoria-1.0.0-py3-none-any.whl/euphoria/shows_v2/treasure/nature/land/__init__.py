


'''
	from euphoria.shows_v2.treasure.nature.land import develop_land
	develop_land ()
'''

'''
	natures:
		This is the amount and identity of the treasures.
	
	measures: 
		These are the sums of the natures.
		
			example, calculated from:
				1.2 packages of sunflower seed + 
				1.6 packages of lentils
	
	grove:
		This is every essential nutrient in the 
		"essential_nutrients" collection.
		
	
'''

from .measures import build_land_measures_foundation

def develop_land ():
	return {
		"natures": [],
		"measures": build_land_measures_foundation (),
		"grove": []
	}