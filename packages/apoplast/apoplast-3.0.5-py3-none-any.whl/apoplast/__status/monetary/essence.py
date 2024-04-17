
'''
	apoplast_1 on --essence-path essence.py
'''

'''
	# near 
	# vicinity
	# not-distant
'''	

'''
	/apoplast_frame
		/monetary
			/_data
			
			the.process_identity_number
			the.logs
		
		/harbor
			the.process_identity_number
'''

import json
fp = open ("/online/vaccines_apoplast/mints/apoplast/ellipsis.JSON", "r")
ellipsis = json.loads (fp.read ())
fp.close ()

def crate (the_path):
	from os.path import dirname, join, normpath
	import sys
	import pathlib
	this_directory = pathlib.Path (__file__).parent.resolve ()
	
	print (this_directory, the_path)
	
	return str (normpath (join (this_directory, the_path)))


print (crate ("here"))


essence = {
	"monetary": {
		"DB_name": "ingredients",
		"URL": "mongodb://0.0.0.0:39000/",
		
		"onsite": {
			"host": "0.0.0.0",
			"port": "39000",
			
			"path": crate ("monetary/_data"),
			"PID_path": crate ("monetary/the.process_identity_number"),
			"logs_path": crate ("monetary/the.logs")
		},
		
		"saves": {
			"path": crate ("monetary/_saves")
		}
	},
	"harbor": {
		"PID_path": crate ("harbor/the.logs")
	},
	"USDA": {
		"food": ellipsis ["USDA"] ["food"]
	},
	"NIH": {
		"supp": ellipsis ["NIH"] ["supp"]
	}
}

