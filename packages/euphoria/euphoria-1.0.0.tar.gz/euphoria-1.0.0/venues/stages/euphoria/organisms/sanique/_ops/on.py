

'''
	from euphoria.organisms.sanique._ops.on as turn_on_sanique
	turn_on_sanique ()
'''

'''
	python3 --shutdown --pidfilepath /var/run/mongodb/mongod.pid
'''

import multiprocessing
import subprocess
import time
import os
import atexit
import shutil
import sys

from ..utilities.has_sanic_check import has_sanic_check

from .status import check_sanique_status

from euphoria._essence import retrieve_essence
	

def floating_process (procedure, CWD, env):
	print ("procedure:", procedure)
	process = subprocess.Popen (
		procedure, 
		cwd = CWD,
		env = env
	)
	
	pid = process.pid
	
	print ("sanic pid:", pid)

def turn_on_sanique ():
	essence = retrieve_essence ()

	has_sanic_check ()

	the_status = check_sanique_status ()
	if (the_status == "on"):
		print ("sanic is already on")		
		return;

	harbor_port = essence ["harbor"] ["port"]
	harbor_path = essence ["harbor"] ["directory"]

	env_vars = os.environ.copy ()
	env_vars ["USDA_food"] = essence ["USDA"] ["food"]
	env_vars ["NIH_supp"] = essence ["NIH"] ["supp"]
	env_vars ['PYTHONPATH'] = ":".join (sys.path)
	
	process = floating_process (
		procedure = [
			"sanic",
			f'harbor:create',
			f'--port={ harbor_port }',
			f'--host=0.0.0.0',
			
			'--fast',
			'--factory',
			
			#'--dev'
		],
		CWD = harbor_path,
		env = env_vars
	)

	return;