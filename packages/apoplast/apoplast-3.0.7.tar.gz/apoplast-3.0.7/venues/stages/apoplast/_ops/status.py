

'''
	import apoplast._interfaces.status as apoplast_status
	apoplast_status.status (
		essence_path = "essence.py"
	)
'''

import apoplast.monetary.status as monetary_status
import apoplast._interfaces.sanique.status as sanic_status

from apoplast._essence import prepare_essence
from apoplast._essence import run_script_from_file

import rich

def status (
	essence_path
):	
	apoplast_essence = prepare_essence (
		run_script_from_file (
			essence_path
		)
	)

	if ("onsite" in apoplast_essence ["monetary"]):
		local_mongo_status = monetary_status.status (
			apoplast_essence = apoplast_essence
		)
		
	the_sanic_status = sanic_status.status (
		apoplast_essence = apoplast_essence
	)
	
	the_status = {
		"monetary": {
			"local": local_mongo_status
		},
		"sanique": {
			"local": the_sanic_status
		}
	}
	
	print ()
	rich.print_json (data = {
		"status": the_status
	})
	
	return the_status