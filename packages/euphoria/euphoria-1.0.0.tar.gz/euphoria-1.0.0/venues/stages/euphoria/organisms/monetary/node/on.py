

'''
	mongod --dbpath ./../_mongo_data --port 39000
'''

'''
	from euphoria.monetary.node.on import turn_on_monetary_node
	mongo_process = turn_on_monetary_node (
		euphoria_essence = euphoria_essence,
		
		exception_if_on = True
	)
	
	import time
	while True:
		time.sleep (1)
'''

'''	
	mongo_process.terminate ()

	#
	#	without this it might appear as if the process is still running.
	#
	import time
	time.sleep (2)
'''





from ..status import find_monetary_status
	
import euphoria.mixes.procedure as procedure
from euphoria._essence import retrieve_essence
	
	
	
import ships.cycle.loops as cycle_loops	
	
import rich
	
from fractions import Fraction
import multiprocessing
import subprocess
import time
import os
import atexit

def turn_on_monetary_node (
	exception_if_on = False
):
	essence = retrieve_essence ()

	print ()
	print ("checking if the monetary is already on")
	print ()

	the_monetary_status = find_monetary_status ()
	if (the_monetary_status == "on"):
		print ("The monetary is already on")
		return;

	port = essence ["monetary"] ["onsite"] ["port"]
	dbpath = essence ["monetary"] ["onsite"] ["path"]
	PID_path = essence ["monetary"] ["onsite"] ["PID_path"]
	logs_path = essence ["monetary"] ["onsite"] ["logs_path"]

	os.makedirs (dbpath, exist_ok = True)
	os.makedirs (os.path.dirname (logs_path), exist_ok = True)
	os.makedirs (os.path.dirname (PID_path), exist_ok = True)

	script = [
		"mongod", 

		'--fork',

		'--dbpath', 
		#f"'{ dbpath }'", 
		f"{ dbpath }", 
		
		'--logpath',
		f"{ logs_path }", 
	
		
		'--port', 
		str (port),
		
		'--bind_ip',
		'0.0.0.0',
		
		'--pidfilepath',
		str (PID_path)
	]

	rich.print_json (data ={
		"procedure": script
	})

	mongo_process = procedure.implicit (script)


	the_monetary_status_2 = monetary_status.status (
		loop_limit = 5
	)
	if (the_monetary_status_2 == "on"):
		exception_strand = "The monetary is already on"
	
		if (exception_if_on):
			raise Exception (exception_strand)
	
		print (exception_strand)
		return mongo_process

	raise Exception ("A connection to the monetary could not be established.")
	
	


#
#
#