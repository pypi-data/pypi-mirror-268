



'''
	status_chia_seeds_214893
'''
'''
	python3 insurance.py clouds/supp_NIH/nature/_status/powder/status_mane_270619.py
'''

import apoplast.clouds.supp_NIH.nature as supp_NIH_nature
import apoplast.clouds.supp_NIH.examples as NIH_examples

import json

def check_1 ():	
	supp_1 = supp_NIH_nature.create (
		NIH_examples.retrieve ("powder/mane_270619.JSON")
	)
	
	def add (path, data):
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = pathlib.Path (__file__).parent.resolve ()
		example_path = normpath (join (this_directory, path))
		FP = open (example_path, "w")
		FP.write (data)
		FP.close ()
		
	add ("mane_270619_nature.JSON", json.dumps (supp_1, indent = 4))
	
	return;
	
checks = {
	"check 1": check_1
}