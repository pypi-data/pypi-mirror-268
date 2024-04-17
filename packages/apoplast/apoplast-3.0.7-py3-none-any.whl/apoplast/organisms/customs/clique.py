


import apoplast.organisms.customs as build_customs
	
import click
import time

def clique ():
	customs = build_customs ()

	@click.group ("customs")
	def group ():
		pass

	@group.command ("on")
	#@click.option ('--example-option', required = True)
	def on ():
		customs ["on"] ()
		
		

	@group.command ("off")
	#@click.option ('--example-option', required = True)
	def off ():
		customs ["off"] ()
		
		
	@group.command ("status")
	#@click.option ('--example-option', required = True)
	def on ():
		customs ["status"] ()


	return group




#



