
'''
	sanic inspect shutdown
'''

'''
	import euphoria._interfaces.sanique.status as sanic_status
	the_status = sanic_status.status (
		essence = prepare_essence ({})
	)
	
	# "on" "off"
'''

import multiprocessing
import subprocess
import time
import os
import atexit

from ..utilities.has_sanic_check import has_sanic_check

import requests
import rich

def background (procedure, CWD):
	print ("procedure:", procedure)
	process = subprocess.Popen (procedure, cwd = CWD)


def check_sanique_status ():
	essence = retrieve_essence ()

	has_sanic_check ()

	host = essence ["harbor"] ["inspector"] ["host"]
	port = essence ["harbor"] ["inspector"] ["port"]
	
	URL = f"http://{ host }:{ port }"
	
	try:
		response = requests.get (URL)
		if response.status_code == 200:
			data = response.json ()
			rich.print_json (data = data)
			
			return "on"
		
		else:
			print("Error:", response.status_code)
	
	except Exception as E:
		print ("exception:", E)

	return "off"