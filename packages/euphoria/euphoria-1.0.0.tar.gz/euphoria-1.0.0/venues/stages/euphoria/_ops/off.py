

'''
	import euphoria._interfaces.off as euphoria_off
	euphoria_off.off (
		essence_path = "essence.py"
	)
'''

import euphoria.monetary.off as monetary_off
import euphoria._interfaces.sanique.off as sanic_off

from euphoria._essence import prepare_essence
from euphoria._essence import run_script_from_file

def off (
	essence_path
):	
	euphoria_essence = prepare_essence (
		run_script_from_file (essence_path)
	)
	if ("onsite" in euphoria_essence ["monetary"]):
		mongo_process = monetary_off.off (
			euphoria_essence = euphoria_essence
		)
	
	sanic_off.off (
		euphoria_essence = euphoria_essence
	)
	
	