
import pathlib
from os.path import dirname, join, normpath
import sys
import os
import time

from euphoria._essence import prepare_essence
from euphoria._essence import run_script_from_file
import euphoria.mixes.procedure as procedure

import click
import rich



def monetary_memories_clique ():
	
	@click.group ("memories")
	def group ():
		pass
	
	'''
		# save
		# scan
		# remember
	'''
	'''
		itinerary:
			[ ] euphoria_1 monetary structures export --export-name export.2.json
	'''
	@group.command ("export")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria monetary structures --essence-path essence.py', 
		required = False
	)
	def save (essence_path):
		euphoria_essence = prepare_essence (
			run_script_from_file (
				essence_path
			)
		)
		
		the_exports_path = euphoria_essence ["monetary"] ["saves"] ["exports"] ["path"]
	
	
	'''
		euphoria_1 monetary structures import --import-name export.1.json
	'''
	@group.command ("import")
	@click.option (
		'--essence-path', 
		default = 'essence.py',
		help = 'euphoria monetary structures --essence-path essence.py', 
		required = False
	)
	@click.option (
		'--import-name',
		required = True
	)
	@click.option (
		'--DB',
		default = 'ingredients'
	)
	@click.option (
		'--drop',
		help = "drop the current documents in the collection",
		default = True
	)
	def insert (essence_path, import_name, db, drop):
		euphoria_essence = prepare_essence (
			run_script_from_file (
				essence_path
			)
		)
		
		the_exports_path = euphoria_essence ["monetary"] ["saves"] ["exports"] ["path"]
		the_exports_collections = euphoria_essence ["monetary"] ["saves"] ["exports"] ["collections"]
		
		not_found = []
		
		for collection in the_exports_collections:
			export_path = str (normpath (join (the_exports_path, collection, import_name)))
			if (os.path.exists (export_path) != True):
				not_found.append (export_path)
				continue;

			script = [
				"mongoimport",
				"--uri",
				"mongodb://localhost:39000",
				f"--db={ db }",
				f"--collection={ collection }",
				f"--file={ export_path }"
			]
			
			if (drop):
				script.append ('--drop')
				
			print (" ".join (script))	
				
			procedure.go (
				script = script
			)
			
			time.sleep (1)
		
			
		
		rich.print_json (data = {
			"not found": not_found
		})
		
		
		
		
		
		# mongoimport --uri "mongodb://localhost:39000" --db=ingredients_2 --collection=essential_nutrients --file=essential_nutrients.1.json
	
		return;
	

	return group




#



