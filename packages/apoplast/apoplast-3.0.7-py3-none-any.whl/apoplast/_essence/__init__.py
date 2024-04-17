

'''
	from apoplast._essence import prepare_essence
	apoplast_essence = prepare_essence ({
		"monetary": {
			"name": "apoplast ingredients",
			"port": "39001"
		}
	})
'''

'''
	itinerary:
		[ ] harbor pid for starting and stopping:
				"PID_path": crate ("harbor/the.process_identity_number")
'''

'''
	from apoplast._essence import run_script_from_file
	run_script_from_file ("")
'''

'''
# receive_monetary_URL
from apoplast._essence import receive_monetary_URL
monetary_URL = receive_monetary_URL (
	apoplast_essence = apoplast_essence
)
'''

import pathlib
from os.path import dirname, join, normpath
import sys
import os

import rich
import pydash


def find_essence ():
	return;

def receive_monetary_URL (
	apoplast_essence = {}
):
	if ("URL" in apoplast_essence ["monetary"]):
		return apoplast_essence ["monetary"] ["URL"]

	return "mongodb://" + apoplast_essence ["monetary"] ["host"] + ":" + apoplast_essence ["monetary"] ["port"] + "/"

def run_script_from_file (
	file_path
):
	with open (file_path, 'r') as file:
		script_content = file.read ()
        
	proceeds = {}	
		
	exec (script_content, {
		'__file__': os.getcwd () + "/" + os.path.basename (file_path)
	}, proceeds)
	
	essence = proceeds ['essence']
	
	return essence;

def prepare_essence_from_py_file (essence_path):
	return prepare_essence (
		run_script_from_file (
			essence_path
		)
	)

def prepare_essence (
	essence = {}
):
	this_folder = pathlib.Path (__file__).parent.resolve ()	

	the_merged_essence = pydash.merge (
		{
			"monetary": {
				#
				#	optional: URL
				#
				"DB_name": "ingredients",
				
				#
				#	_saves
				#		
				#
				"saves": {
					"path":  str (normpath (join (this_folder, "../monetary/ingredients_DB/_the_saves"))),
					
					"exports": {
						"path": str (normpath (join (this_folder, "../monetary/ingredients_DB/_the_saves/exports"))),
						"collections": [
							"cautionary_ingredients",
							"essential_nutrients",
							"glossary"
						]
					},
					"dumps": {
						"path": str (normpath (join (this_folder, "../monetary/ingredients_DB/_the_saves/dumps"))),
					}					
				}
			},
			"harbor": {
				"directory": str (normpath (join (this_folder, "../_interfaces/sanique"))),
				"path": str (normpath (join (this_folder, "../_interfaces/sanique/harbor.py"))),
				
				#
				#	don't modify these currently
				#
				#	These are used for retrieval, but no for launching the
				#	sanic inspector.
				#
				#	https://sanic.dev/en/guide/running/inspector.md#inspector
				#
				"inspector": {
					"port": "6457",
					"host": "0.0.0.0"
				}
			},
			
			
			
		},
		essence
	)
	
	rich.print_json (data = {
		"apoplast_essence": the_merged_essence
	})
	
	
	return the_merged_essence