

'''
	import euphoria.organisms._regula.on as euphoria_on
	euphoria_on.on (
		essence_path = "essence.py"
	)
'''

from euphoria.organisms.sanique._ops.on import turn_on_sanique
from euphoria.organisms.monetary.node.on import turn_on_monetary_node
	
from euphoria._essence import retrieve_essence

import rich

def on ():	
	essence = retrieve_essence ()

	rich.print_json (data = essence)

	if ("onsite" in essence ["monetary"]):
		turn_on_monetary_node ()
		
	turn_on_sanique ()	
		
	'''
	sanic_on.on (
		euphoria_essence = euphoria_essence
	)
	'''