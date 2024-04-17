
'''
	from euphoria.monetary.ingredients.DB.off import turn_off_monetary_node
	mongo_process = turn_off_monetary_node (
		euphoria_essence = euphoria_essence
	)
'''

'''
	mongod --shutdown --pidfilepath /var/run/mongodb/mongod.pid
'''

import multiprocessing
import subprocess
import time
import os
import atexit

import euphoria.mixes.procedure as procedure

def turn_off_monetary_node (
	euphoria_essence = {},
	exception_if_off = False
):
	#port = euphoria_essence ["monetary"] ["onsite"] ["port"]
	dbpath = euphoria_essence ["monetary"] ["onsite"] ["path"]
	PID_path = euphoria_essence ["monetary"] ["onsite"] ["PID_path"]
	#logs_path = euphoria_essence ["monetary"] ["onsite"] ["logs_path"]
	
	mongo_process = procedure.implicit ([
		"mongod",
		"--shutdown",
		
		'--dbpath', 
		f"{ dbpath }", 
		
		"--pidfilepath",
		f"'{ PID_path }'"
	])
	
	
	
	
	return;