

'''
	python3 /apoplast/venues/stages/apoplast/__status_monetary/monetary_status.proc.py
'''

'''
	mongo connection strings
		
		DB: apoplast
			
			collection: 
				cautionary_ingredients
				essential_nutrients
'''



def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_directory = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_directory, path)))
		print ("added paths:", normpath (join (this_directory, path)))
	

add_paths_to_system ([
	'../../../stages',
	'../../../stages_pip'
])


import json
import pathlib
from os.path import dirname, join, normpath
import sys
import biotech

this_directory = pathlib.Path (__file__).parent.resolve ()
the_essence_path = str (normpath (join (this_directory, "essence.py")))

'''
	make sure that it is off
'''
import apoplast._interfaces.on as apoplast_on
import apoplast._interfaces.off as apoplast_off
import apoplast._interfaces.status as apoplast_status
		

the_apoplast_status = apoplast_status.status (
	essence_path = the_essence_path
)
assert (the_apoplast_status ["monetary"] ["local"] == "no"), the_apoplast_status
assert (the_apoplast_status ["sanique"] ["local"] == "no"), the_apoplast_status

apoplast_on.on (
	essence_path = the_essence_path
)


'''
#import apoplast.monetary.ingredients.DB.open as ingredient_DB
mongo_process = ingredient_DB.open (
	apoplast_essence = apoplast_essence
)
'''
def start_scan ():
	name = "apoplast"
	
	venues = str (normpath (join (this_directory, "../../../../venues")))
	this_stage = str (normpath (join (venues, f"stages/{ name }")))

	if (len (sys.argv) >= 2):
		glob_string = this_stage + '/' + sys.argv [1]
		db_directory = False
	else:
		glob_string = this_stage + '/**/monetary_status_*.py'
		db_directory = normpath (join (this_directory, "db"))

	print ("glob string:", glob_string)

	scan = biotech.start (
		glob_string = glob_string,
		
		simultaneous = True,
		simultaneous_capacity = 2,
		
		module_paths = [
			normpath (join (venues, "stages")),
			normpath (join (venues, "stages_pip"))
		],
		relative_path = this_stage,
		
		db_directory = db_directory,
		
		aggregation_format = 2
	)
	
	return scan


scan_proceeds = start_scan ()



apoplast_off.off (
	essence_path = the_essence_path
)