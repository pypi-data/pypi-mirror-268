

'''
	This is for starting sanique in floating (or implicit) mode.
'''


import euphoria._interfaces.sanique.on as sanic_on
import euphoria._interfaces.sanique.off as sanic_off
import euphoria._interfaces.sanique.status as sanic_status

from euphoria._essence import prepare_essence
from euphoria._essence import run_script_from_file
	
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
		help = 'euphoria sanique on --essence-path essence.py', 
		required = False
	)
	def on (essence_path):			
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		euphoria_essence = prepare_essence (run_script_from_file (essence_path))
		
		sanic_on.on (
			euphoria_essence = euphoria_essence
		)
		
		time.sleep (1)
		

	@group.command ("off")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria sanique on --essence-path essence.py', 
		required = False
	)
	def off (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		euphoria_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"euphoria_essence": euphoria_essence
		})
		sanic_off.off (
			euphoria_essence = euphoria_essence
		)
		
		time.sleep (1)
		
		
	@group.command ("status")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria sanique on --essence-path essence.py', 
		required = False
	)
	def status (essence_path):
		essence_full_path = str (normpath (join (os.getcwd (), "essence")))
		euphoria_essence = prepare_essence (run_script_from_file (essence_path))
		rich.print_json (data = {
			"euphoria_essence": euphoria_essence
		})
		
		sanic_status.status (
			euphoria_essence = euphoria_essence
		)
		
		time.sleep (1)

	return group




#



