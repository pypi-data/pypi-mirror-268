

'''
	mongod --dbpath ./../_mongo_data --port 39000
'''

'''
	import apoplast.monetary.status as monetary_status
	the_monetary_status = monetary_status.status (
		apoplast_essence = apoplast_essence
	)
	
	import time
	while True:
		time.sleep (1)
'''

'''	
	mongo_process.terminate ()

	#
	#	without this it might appear as if the process is still running.
	#
	import time
	time.sleep (2)
'''

from fractions import Fraction
import multiprocessing
import subprocess
import time
import os
import atexit

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import ServerSelectionTimeoutError
import rich

from apoplast._essence import receive_monetary_URL

import ships.cycle as cycle

def find_monetary_status (
	apoplast_essence = {},
	loop_limit = 1
):
	'''
	monetary_URL = receive_monetary_URL (
		apoplast_essence = apoplast_essence
	)
	'''
	
	monetary_URL = apoplast_essence ["monetary"] ["URL"]
	
	print ("checking on URL:", monetary_URL)	
	
	counter = 0
	
	def show (* positionals, ** keywords):
		nonlocal counter
		counter += 1
	
		print (f'connection attempt { counter }', positionals, keywords)
	
		try:
			client = MongoClient (monetary_URL, serverSelectionTimeoutMS=2000)
			
			print ('	client:', client)
			
			client.server_info ()
			print ("	A connection to the monetary was established!")
			
			return "on"
			
		except ConnectionFailure:
			pass;
			
		print ("	A connection to the monetary could not be established!\n")
		
		if (counter == loop_limit):
			return "off"
		
		raise Exception ("")
		
	
	proceeds = cycle.loops (
		show, 
		cycle.presents ([ 1 ]),
		
		#
		#	this is the loop limit
		#
		loops = loop_limit,
		delay = Fraction (1, 1),
		
		records = 0
	)
	
	print ("The monetary is:", proceeds)
	
	
	return proceeds;

	
