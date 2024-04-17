








'''
	python3 insurance.py shows/ingredient_scan/measures/merge/status_1.py
'''

import apoplast.clouds.food_USDA.deliveries.one.assertions.foundational as assertions_foundational
import apoplast.clouds.food_USDA.examples as USDA_examples	
import apoplast.clouds.food_USDA.nature as food_USDA_nature
import apoplast.mixes.insure.equality as equality

import apoplast.shows.ingredient_scan.measures.multiply as multiply_measures
import apoplast.shows.ingredient_scan.measures.merge as merge_measures
	
import json	

def check_1 ():
	aggregate_measures = {
		"mass + mass equivalents": {
			"per recipe": {
				"grams": {
					"fraction string": "1000"
				}
			}
		},
		"energy": {
			"per recipe": {
				"food calories": {
					"fraction string": "2000"
				}
			}
		}
	}
	
	new_measures = {
		"mass + mass equivalents": {
			"per recipe": {
				"grams": {
					"fraction string": "4000"
				}
			}
		},
		"energy": {
			"per recipe": {
				"food calories": {
					"fraction string": "1"
				}
			}
		}
	}
	
	merge_measures.calc (
		aggregate_measures,
		new_measures
	)

	assert (
		aggregate_measures == 
		{
			"mass + mass equivalents": {
				"per recipe": {
					"grams": {
						"fraction string": "5000",
						'scinote string': '5.0000e+3'
					}
				}
			},
			"energy": {
				"per recipe": {
					"food calories": {
						"fraction string": "2001",
						'scinote string': '2.0010e+3'
					}
				}
			}
		}
	), aggregate_measures

checks = {
	'check 1': check_1
}