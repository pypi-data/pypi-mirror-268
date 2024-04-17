
'''
	sanic inspect shutdown
'''

'''
	import euphoria._interfaces.sanic.on as sanic_on
	sanic_off.off (
		euphoria_essence = prepare_essence ({})
	)
'''

'''
	objectives:
		[ ] implicit
'''

import multiprocessing
import subprocess
import time
import os
import atexit

from .has_sanic_check import has_sanic_check
from .status import status as sanic_status
	

def background (procedure, CWD):
	print ("procedure:", procedure)
	process = subprocess.Popen (procedure, cwd = CWD)


def off (
	euphoria_essence = {}
):
	essence = retrieve_essence ()

	print (euphoria_essence)

	has_sanic_check ()

	the_status = sanic_status (
		euphoria_essence = euphoria_essence
	)
	if (the_status == "off"):
		print ('sanique is already off')
		return

	harbor_path = euphoria_essence ["harbor"] ["directory"]
	process = background (
		procedure = [
			"sanic",
			"inspect",
			"shutdown"
		],
		CWD = harbor_path
	)

	return;