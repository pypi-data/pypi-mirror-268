

'''
	import euphoria._interfaces.status as euphoria_status
	euphoria_status.status (
		essence_path = "essence.py"
	)
'''

import euphoria.monetary.status as monetary_status
import euphoria._interfaces.sanique.status as sanic_status

from euphoria._essence import prepare_essence
from euphoria._essence import run_script_from_file

import rich

def status (
	essence_path
):	
	euphoria_essence = prepare_essence (
		run_script_from_file (
			essence_path
		)
	)

	if ("onsite" in euphoria_essence ["monetary"]):
		local_mongo_status = monetary_status.status (
			euphoria_essence = euphoria_essence
		)
		
	the_sanic_status = sanic_status.status (
		euphoria_essence = euphoria_essence
	)
	
	the_status = {
		"monetary": {
			"local": local_mongo_status
		},
		"sanique": {
			"local": the_sanic_status
		}
	}
	
	print ()
	rich.print_json (data = {
		"status": the_status
	})
	
	return the_status