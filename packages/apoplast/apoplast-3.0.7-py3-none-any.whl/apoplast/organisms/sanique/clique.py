

'''
	This is for starting sanique in floating (or implicit) mode.
'''


import apoplast._interfaces.sanique.on as sanic_on
import apoplast._interfaces.sanique.off as sanic_off
import apoplast._interfaces.sanique.status as sanic_status

from apoplast._essence import prepare_essence
from apoplast._essence import run_script_from_file
	
import click
import rich

import time
import os
import pathlib
from os.path import dirname, join, normpath
import sys

def clique ():

	@click.group ("sanique")
	def group ():
		pass


	@group.command ("on")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'apoplast sanique on --essence-path essence.py', 
		required = False
	)
	def on (essence_path):			
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		apoplast_essence = prepare_essence (run_script_from_file (essence_path))
		
		sanic_on.on (
			apoplast_essence = apoplast_essence
		)
		
		time.sleep (1)
		

	@group.command ("off")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'apoplast sanique on --essence-path essence.py', 
		required = False
	)
	def off (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		apoplast_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"apoplast_essence": apoplast_essence
		})
		sanic_off.off (
			apoplast_essence = apoplast_essence
		)
		
		time.sleep (1)
		
		
	@group.command ("status")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'apoplast sanique on --essence-path essence.py', 
		required = False
	)
	def status (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		apoplast_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"apoplast_essence": apoplast_essence
		})
		
		sanic_status.status (
			apoplast_essence = apoplast_essence
		)
		
		time.sleep (1)

	return group




#



