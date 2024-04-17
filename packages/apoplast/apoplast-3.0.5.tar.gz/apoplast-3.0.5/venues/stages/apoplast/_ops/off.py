

'''
	import apoplast._interfaces.off as apoplast_off
	apoplast_off.off (
		essence_path = "essence.py"
	)
'''

import apoplast.monetary.off as monetary_off
import apoplast._interfaces.sanique.off as sanic_off

from apoplast._essence import prepare_essence
from apoplast._essence import run_script_from_file

def off (
	essence_path
):	
	apoplast_essence = prepare_essence (
		run_script_from_file (essence_path)
	)
	if ("onsite" in apoplast_essence ["monetary"]):
		mongo_process = monetary_off.off (
			apoplast_essence = apoplast_essence
		)
	
	sanic_off.off (
		apoplast_essence = apoplast_essence
	)
	
	