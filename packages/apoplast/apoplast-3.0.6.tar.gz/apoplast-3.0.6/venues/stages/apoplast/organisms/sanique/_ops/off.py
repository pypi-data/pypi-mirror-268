
'''
	sanic inspect shutdown
'''

'''
	import apoplast._interfaces.sanic.on as sanic_on
	sanic_off.off (
		apoplast_essence = prepare_essence ({})
	)
'''

'''
	objectives:
		[ ] implicit
'''

import multiprocessing
import subprocess
import time
import os
import atexit

from .has_sanic_check import has_sanic_check
from .status import status as sanic_status
	

def background (procedure, CWD):
	print ("procedure:", procedure)
	process = subprocess.Popen (procedure, cwd = CWD)


def off (
	apoplast_essence = {}
):
	print (apoplast_essence)

	has_sanic_check ()

	the_status = sanic_status (
		apoplast_essence = apoplast_essence
	)
	if (the_status == "off"):
		print ('sanique is already off')
		return

	harbor_path = apoplast_essence ["harbor"] ["directory"]
	process = background (
		procedure = [
			"sanic",
			"inspect",
			"shutdown"
		],
		CWD = harbor_path
	)

	return;