



'''
	from euphoria._essence import retrieve_essence
	essence = retrieve_essence ()
'''

'''
	from euphoria._essence import build_essence
	build_essence ()
'''


'''
	from euphoria._essence import prepare_essence
	euphoria_essence = prepare_essence ({
		"monetary": {
			"name": "euphoria ingredients",
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
	from euphoria._essence import run_script_from_file
	run_script_from_file ("")
'''

'''
	# receive_monetary_URL
	from euphoria._essence import receive_monetary_URL
	monetary_URL = receive_monetary_URL (
		euphoria_essence = euphoria_essence
	)
'''

import pathlib
from os.path import dirname, join, normpath
import sys
import os

import rich
import pydash

essence = {}

#
#	Use this; that way can easily
# 	start using redis or something.
#
def retrieve_essence ():
	return essence

def build_essence ():
	CWD = os.getcwd ()
	possible_location = str (normpath (join (CWD, "essence.py")));

	the_merged_essence = prepare_essence_from_py_file (
		possible_location
	)
	
	for key in the_merged_essence:
		essence [ key ] = the_merged_essence [key]
		
	print ('essence built')

def receive_monetary_URL ():
	if ("URL" in essence ["monetary"]):
		return essence ["monetary"] ["URL"]

	return "mongodb://" + essence ["monetary"] ["host"] + ":" + essence ["monetary"] ["port"] + "/"

def run_script_from_file (file_path):
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
			"sanique": {
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
	
	#rich.print_json (data = {
	#	"euphoria_essence": the_merged_essence
	#})
	
	
	return the_merged_essence