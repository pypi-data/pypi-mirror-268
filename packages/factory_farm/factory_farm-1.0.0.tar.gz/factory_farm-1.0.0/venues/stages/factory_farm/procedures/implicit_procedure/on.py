
'''
	from factory_farm.procedures.implicit_procedure.on import implicit_procedure_on
	implicit_procedure_on ()
'''

'''
	picks:
		( ) sequentially
		( ) simultaneously
		( ) one
'''



'''
	This script starts the keg process.
'''

from botanist.cycle.presents import presents as cycle_presents
import botanist.processes.multiple as multi_proc
import botanist.cycle.loops as cycle_loops
import botanist.ports_v2.available as available_port

from factory_farm.topics.process_on.p_expect import process_on
from factory_farm.topics.process_on.p_expect.implicit import process_on_implicit

from .paths import find_implicit_procedure_paths
		
# ----

import pexpect
import rich

# ----

import sys
import json
import os
from fractions import Fraction
import time

# ----

def implicit_procedure_on (
	port,
	packet
):
	limit_start = 25000
		
	path_of_the_scan_process = find_implicit_procedure_paths ()
	process_string = (
		f'''python3 { path_of_the_scan_process } keg open --port { port }'''
	)
	
	process_environment = os.environ.copy ()
	process_environment ["PYTHONPATH"] = ":".join ([
		* sys.path
	])

	the_venture = process_on_implicit (
		process_string,
		
		CWD = None,
		env = process_environment,
		name = "aggregator"
	)
	
	time.sleep (1)
	print ('the implicit procedure:', the_venture)

	return the_venture

	'''
	procs = multi_proc.start (
		processes = [{
			"string": process_string,
			"CWD": None,
			"ENV": process_environment
		}]
	)
	'''

		

	