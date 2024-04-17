



#from euphoria.organisms.monetary.clique import clique as monetary_clique
#from euphoria.organisms.customs.clique import clique as customs_clique
#from euphoria.organisms.sanique.clique import clique as sanic_clique

import euphoria._ops.on as euphoria_on
#import euphoria._ops.off as euphoria_off
#import euphoria._ops.status as euphoria_status

#from euphoria._essence import prepare_essence_from_py_file

from euphoria._essence import build_essence, retrieve_essence

from euphoria._essence import essence

import somatic

import os
import json
import time
import pathlib
from os.path import dirname, join, normpath
import sys

import rich
import click

this_directory = pathlib.Path (__file__).parent.resolve ()	

def clique ():
	'''
		Check for essence here and then set them 
		implicitly.
	'''
	print ('essence check')
	build_essence ()
	


	@click.group ()
	def group ():
		pass

	@click.command ("help")
	def help ():	
		the_mix = str (normpath (join (this_directory, "../..")))
		
		somatic.start ({
			"directory": the_mix,
			"relative path": the_mix,
			"port": 20000,
			"static port": False,
			"verbose": 1
		})

		import time
		while True:
			time.sleep (1000)
	
	
	#
	#	euphoria on
	#
	@click.command ("essence")
	def print_essence ():	
		essence = retrieve_essence ()
		rich.print_json (data = essence)
	
	#
	#	euphoria on
	#
	@click.command ("on")
	def on ():		
		euphoria_on.on ()

	
	
	'''
	@click.command ("off")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria off --essence-path essence.py', 
		required = False
	)
	def off (essence_path):
		euphoria_off.off (essence_path)
		time.sleep (2)
		print ('off')
		
	@click.command ("status")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria off --essence-path essence.py', 
		required = False
	)
	def status (essence_path):
		euphoria_status.status (essence_path)
		time.sleep (2)

		
	

	
	group.add_command (off)
	group.add_command (status)
	'''
	
	
	
	group.add_command (help)
	
	group.add_command (on)
	group.add_command (print_essence)
		
	#group.add_command (monetary_clique ())
	#group.add_command (sanic_clique ())
	#group.add_command (customs_clique ())
	
	group ()




#
