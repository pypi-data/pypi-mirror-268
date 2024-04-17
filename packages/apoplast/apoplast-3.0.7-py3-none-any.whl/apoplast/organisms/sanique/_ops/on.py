

'''
	import apoplast._interfaces.sanique.on as sanique_on
	sanic_on.on (
		apoplast_essence = prepare_essence ({})
	)
'''

'''
	python3 --shutdown --pidfilepath /var/run/mongodb/mongod.pid
'''

import multiprocessing
import subprocess
import time
import os
import atexit
import shutil
import sys

from .has_sanic_check import has_sanic_check
import apoplast._interfaces.sanique.status as sanique_status

def background (procedure, CWD, env):
	print ("procedure:", procedure)
	process = subprocess.Popen (
		procedure, 
		cwd = CWD,
		env = env
	)
	
	pid = process.pid
	
	print ("sanic pid:", pid)

def on (
	apoplast_essence = {}
):
	has_sanic_check ()

	the_status = sanique_status.status (
		apoplast_essence = apoplast_essence
	)
	if (the_status == "on"):
		print ("sanic is already on")		
		return;

	harbor_port = apoplast_essence ["harbor"] ["port"]
	harbor_path = apoplast_essence ["harbor"] ["directory"]

	env_vars = os.environ.copy ()
	env_vars ["USDA_food"] = apoplast_essence ["USDA"] ["food"]
	env_vars ["NIH_supp"] = apoplast_essence ["NIH"] ["supp"]
	env_vars ['PYTHONPATH'] = ":".join (sys.path)
	
	process = background (
		procedure = [
			"sanic",
			f'harbor:create',
			f'--port={ harbor_port }',
			f'--host=0.0.0.0',
			
			'--fast',
			'--factory',
			
			#'--dev'
		],
		CWD = harbor_path,
		env = env_vars
	)

	return;