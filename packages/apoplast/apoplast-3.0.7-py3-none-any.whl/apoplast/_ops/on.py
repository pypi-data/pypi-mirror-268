

'''
	import apoplast.organisms._regula.on as apoplast_on
	apoplast_on.on (
		essence_path = "essence.py"
	)
'''

import apoplast.organisms.monetary.on as monetary_on
import apoplast.organisms.sanique.on as sanic_on

from apoplast._essence import prepare_essence
from apoplast._essence import run_script_from_file

def on (apoplast_essence):	
	if ("onsite" in apoplast_essence ["monetary"]):
		mongo_process = monetary_on.on (
			apoplast_essence = apoplast_essence
		)
		
	sanic_on.on (
		apoplast_essence = apoplast_essence
	)