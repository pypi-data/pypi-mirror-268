
'''
	from factory_farm.topics.process_on.p_expect.implicit import process_on_implicit
	
	venture = process_on_implicit (
		'',
		
		CWD = None,
		env = {}
	)
	
	#
	# status
	#
	#
	print ('status:', venture ["process"].is_alive ())
	
	#
	#	stop the process
	#
	#
	venture ["process"].terminate ()
	
	records = venture ["records"] ()
'''

from factory_farm.topics.process_on.p_expect import process_on

import pexpect
import rich

import atexit
import os
from multiprocessing import Process, Queue
import multiprocessing


def process_on_implicit (
	process_string,
	
	the_queue = None,
	CWD = None,
	env = {},
	
	name = "process"
):
	the_queue = Queue ()

	stop_event = multiprocessing.Event ()

	implicit_process = Process (
		target = process_on,
		
		args = [ 
			process_string 
		],
		
		kwargs = {
			"the_queue": the_queue,
			"CWD": CWD,
			"env": env,
			"name": name,
			
			"stop_event": stop_event
		}
	)
	
	implicit_process.start ()
	
	# print ('the process started in the implicit')
	
	# if you'd like to await the process
	# implicit_process.join()
	
	#result = the_queue.get (timeout = 1)
	#print ("Result from implicit process:", result)
	
	def parse_queue ():
		proceeds = []
		while not the_queue.empty ():
			proceeds.append (the_queue.get ())
	
		return proceeds;
	
		#return the_queue.get (timeout = 1)
	
	def off ():
		nonlocal stop_event;
		stop_event.set ()
	
	return {
		"process": implicit_process,
		"records": parse_queue,
		"off": off
	}
	
	