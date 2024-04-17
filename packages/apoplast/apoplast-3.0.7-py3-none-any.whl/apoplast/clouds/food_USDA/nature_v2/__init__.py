




'''
	Details about this can be found in "apoplast.shows.nature".
'''


'''
	#
	#	This retrieves a food's data from USDA.	
	#
	import apoplast.clouds.food_USDA.deliveries.one as retrieve_1_food
	food_USDA = retrieve_1_food.presently ()
	
	#
	#	This parses USDA foods into the nature format.
	#
	#		This should use the shared:
	#			apoplast.shows.natures
	#
	import apoplast.clouds.food_USDA.nature as food_USDA_nature
	nature = food_USDA_nature.create (food_USDA)
'''


'''

'''
import apoplast.shows_v2.treasure.nature._assertions as natures_v2_assertions

'''
	nature_v2 circuits
'''
from ._interpret.packageWeight import calc_package_weight
#
from .measures.form import calculate_form
from .measured_ingredients import build_measured_ingredients
from .unmeasured_ingredients import build_unmeasured_ingredients

from .land_essential_nutrients import build_essential_nutrients_land


'''
	python3 libraries
'''
import copy
from fractions import Fraction
import json



def create (
	food_USDA,
	
	return_measured_ingredients_list = False,
	
	records = 0
):
	include_ounces = False
	include_grams = True

	nature = {
		"kind": "food",
		"identity": {
			"name":	food_USDA ["description"],
			"FDC ID": str (food_USDA ["fdcId"]),
			"UPC": food_USDA ["gtinUpc"],
			"DSLD ID": ""
		},
		"brand": {
			"name":	food_USDA ["brandName"],
			"owner": food_USDA ["brandOwner"]
		},
		"measures": {
			"form": {},
			"energy": {
				"ascertained": False,
				"per package": {}
			}
		}
	}
	
	servingSizeUnit = food_USDA ["servingSizeUnit"]

	'''
		treasure exclusive modifications.
	'''
	if (food_USDA ["servingSizeUnit"] == "MLT" and str (food_USDA ["fdcId"]) == "2642759"):
		servingSizeUnit = "mL"
		
	'''
		This calculates the mass and or volume
		from the "packageWeight".
		
		Neither of these are necessary
		for the recipe calculations,
		since supplements don't always
		have these.
	'''
	mass_and_volume = calc_package_weight (food_USDA);
	volume = mass_and_volume ["volume"]
	mass = mass_and_volume ["mass"]
	nature ["measures"]["mass"] = mass
	nature ["measures"]["volume"] = volume

	'''
		{
			"unit": "liter",
			"amount": "473/1000",
			"servings": {
				"listed": {
					"serving size amount": "240",
					"serving size unit": "ml"
				},
				"calculated": {
					"serving size amount": "6/25",
					"servings per package": "473/240"
				}
			}
		}
	'''
	form = calculate_form (
		servingSize = food_USDA ["servingSize"], 
		servingSizeUnit = servingSizeUnit, 
		mass_and_volume = mass_and_volume
	);	
	nature ["measures"] ["form"] = form;
	servings_per_package = form ["servings"]["calculated"]["servings per package"];


	'''
		Measured Ingredients List:
	
			This builds the measured 
			ingredients list.
	'''
	assert ("foodNutrients" in food_USDA)
	nature ["measured ingredients"] = build_measured_ingredients (
		foodNutrients = food_USDA ["foodNutrients"],
		
		mass_and_volume = mass_and_volume,
		form = form,
		
		records = 0
	)
	if (return_measured_ingredients_list):
		return nature ["measured ingredients"]
	
	
	
	'''
		Unmeasured Ingredients List:
			# unreported measurements ingredients
	'''
	nature ["unmeasured ingredients"] = build_unmeasured_ingredients (
		food_USDA = food_USDA
	)
	
	
	'''
		Essential Nutrients
	'''
	'''	
		essential nutrients grove steps:
		
			1. build an "essential nutrients grove"
			2. for each nutrient
	'''	
	nature ["essential nutrients"] = build_essential_nutrients_land (
		copy.deepcopy (nature ["measured ingredients"]),
		
		identity = nature ["identity"]
	)
		

	return nature