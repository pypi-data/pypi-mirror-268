

'''
	the_scan ["process"].is_alive ()
'''

import time
import traceback

import rich
from factory_farm.procedures.implicit_procedure.process.variables import implicit_procedure_variables
from factory_farm.topics.implicit.thread import implicit_thread

from .send_done import send_done
from .aggregate_stats import aggregate_stats
from .stop_process import stop_process

def parse_and_check_is_alive_of_statuses ():
	internal_statuses = implicit_procedure_variables ["internal_statuses"]
	time_limit = implicit_procedure_variables ["intro_variables"] ["time_limit"]

	statuses = {}
	unfinished = []
	for status_path in internal_statuses:
		process_status = "pending"
		
		
		'''
			if over the time limit, stop the process
		'''
		try:
			if (internal_statuses [ status_path ] ["process"] ["process"].is_alive () == True):
				if (time.time () - float (internal_statuses [ status_path ] ["times"] ["started"]) >= float (time_limit)):
					stop_process (
						status_path,
						status = {
							"alarm": "time limit exceeded"
						}
					)
		except Exception as E:
			print ("time limit check exception:", traceback.format_exc ())
			pass;
		
		try:
			#print ("checking process status:", internal_statuses [ status_path ])		
			if (internal_statuses [ status_path ] ["process"] ["process"].is_alive () == False):				
				#
				#	
				#
				#	check if the scan is done, if not the process exitted 
				#	and 
				#
				process_status = "done"
				implicit_procedure_variables ["internal_statuses"] [ status_path ] ["status"] ["process"] = "done"

		except Exception as E:
			print ("parse and check exception:", traceback.format_exc ())
			pass;

		
				
			
		
		except Exception as E:
			pass;
			

		statuses [ status_path ] = {
			"scan": internal_statuses [ status_path ] ["status"] ["scan"],
			"process": process_status
		}
	
	'''
		loop through again,
		because exceptions might
		have occurred.
	'''
	for status_path in statuses:
		if (statuses [ status_path ] ["process"] != "done"):
			unfinished.append (status_path)
		
	return [ statuses, unfinished ]
		

def send_done_if_finished (unfinished):
	if (len (unfinished) >= 1):
		return;
		
	'''
		This loop might be redundant.
	'''
	the_internal_statuses = implicit_procedure_variables ["internal_statuses"]
	for internal_status in the_internal_statuses:
	
		#
		#	if the process is done, then the scan:
		#	
		#		( ) exitted
		#		( ) sent /done_with_scan
		#
		#		( ) unlikely -> neither?
		#
		#if (the_internal_statuses [ internal_status ] [ "status" ] [ "scan" ] != "done"):
		#	return;
	
		if (the_internal_statuses [ internal_status ] [ "status" ] [ "process" ] != "done"):
			return;
	

	'''
		if not bounced, then send done
	'''	
	send_done (
		host = implicit_procedure_variables ["intro_harbor"] ["host"],
		port = implicit_procedure_variables ["intro_harbor"] ["port"],
		
		proceeds = aggregate_stats ()
	)


def print_is_done_status_repetively ():
	details = implicit_procedure_variables ["details"]

	def task (
		stop_event = None
	):		
		while not stop_event.is_set ():
			'''
				check if internal_statuses_built
			'''
			if (implicit_procedure_variables ["internal_statuses_built"] != "yes"):
				continue;
		
			[ internal_statuses, unfinished ] = parse_and_check_is_alive_of_statuses ()
			
			if (details >= 3):
				rich.print_json (
					data = {
						"internal_statuses:": internal_statuses
					}
				)
			
			rich.print_json (
				data = {
					"waiting for:": unfinished
				}
			)
			
			send_done_if_finished (unfinished)
			
			time.sleep (1)
			



	the_task = implicit_thread (
		task = task
	)
	the_task ['on'] ()
	
	# the_task ['on'] ()
	