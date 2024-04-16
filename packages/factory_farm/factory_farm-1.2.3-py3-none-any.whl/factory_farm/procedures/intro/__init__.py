
'''
	import pathlib
	from os.path import dirname, join, normpath
	
	this_folder = pathlib.Path (__file__).parent.resolve ()
	search = normpath (join (this_folder, "../.."))

	import factory_farm
	factory_farm.start (
		glob_string = search + '/**/*status.py'
	)
'''



import glob
import json
import pathlib
from os.path import dirname, join, normpath
import os
import time

import rich	
from tinydb import TinyDB, Query

#import factory_farm.topics.aggregate as aggregate
#import factory_farm.topics.alarm_parser as alarm_parser

#import factory_farm.procedures.scan as scan
#from factory_farm.procedures.scan.on_one import turn_on_one
#from factory_farm.procedures.scan.on_sequentially import turn_on_sequentially
#from factory_farm.procedures.scan.on_simultaneously import turn_on_simultaneously

from factory_farm.topics.printout.passes import printout_passes

# import factory_farm.procedures.regulators.on as regulators_on

from factory_farm.procedures.implicit_procedure.on import implicit_procedure_on

from factory_farm.procedures.intro.keg import open_harbor
from factory_farm.procedures.intro.coms.implicit_procedure.on import await_implicit_procedure_is_on
from factory_farm.procedures.intro.coms.implicit_procedure.send_paths import send_paths

import threading
'''
	
'''
def start (
	glob_string = "",
	
	#
	#	itinerary: optionally dynamic
	#
	intro_port = 52434,
	implicit_procedure_port = 52435,
	
	print_alarms = True,
	records = 1,
	db_directory = False,
	
	aggregation_format = 1,
	
	relative_path = False,
	module_paths = [],
	
	simultaneous = False,
	simultaneous_capacity = 10,
	
	time_limit = "99999999999999999999999",
	
	before = False,
	after = False
):
	#regulators_on.on ()
	#return;



	finds = glob.glob (glob_string, recursive = True)
	relative_path = str (relative_path)	
		
	if (records >= 2):
		print ()
		print ("searching for glob_string:")
		print ("	", glob_string)
		print ()
	
	if (records >= 2):
		print ()
		print ("	finds:", finds)
		print ("	finds count:", len (finds))
		print ();

	wait_until_health_scans_done = threading.Event ()

	
	the_scan_results = {}
	
	def health_scans_done (the_packet):
		nonlocal the_scan_results;
		
		the_scan_results = the_packet
	
		#print ("health_scans_done ->", the_packet)
		#print ("health_scans_done:", wait_until_health_scans_done, wait_until_health_scans_done.is_set ())
		
		wait_until_health_scans_done.set ()
		#print ("health_scans_done:", wait_until_health_scans_done, wait_until_health_scans_done.is_set ())

		#print ("await_health_scans_done set")
		#print ()

	[ intro_harbor ] = open_harbor (
		port = intro_port,
		health_scans_done = health_scans_done
	)	
	intro_harbor.start ()

	the_implicit_procedure = implicit_procedure_on (	
		port = implicit_procedure_port,
		packet = {}
	)
	
	#time.sleep (1)
	
	
	'''
		check if the implicit procedure is on
	'''
	await_implicit_procedure_is_on (
		port = implicit_procedure_port
	)
	print ("the implicit procedure has started")
	
	#time.sleep (1)
	
	send_paths (
		port = implicit_procedure_port,
		packet = {
			"status_check_paths": finds,
			
			"relative_path": relative_path,
			"module_paths": module_paths,
			
			"simultaneous": simultaneous,
			"simultaneous_capacity": simultaneous_capacity,
			
			"before": before,
			"after": after,
			
			"aggregation_format": aggregation_format,
			
			"time_limit": time_limit,
			
			"the_intro_harbor": {
				"port": intro_port,
				"host": "0.0.0.0"
			}
		}
	)	
	
	print ()
	print ("paths sent, waiting until the scans are done.")
	print ()
	
	wait_until_health_scans_done.wait ()
	
	print ()
	print ('done awaiting health scans')
	print ()

	intro_harbor.stop ()
	print ('intro harbor is off')

	print ("the_implicit_procedure:", the_implicit_procedure)

	the_implicit_procedure ["process"].terminate ()

	print ("the_implicit_procedure:", the_implicit_procedure)

	rich.print_json (
		data = {
			"intro: the_scan_results": the_scan_results 
		}
	)
	
	if (type (db_directory) == str):
		os.makedirs (db_directory, exist_ok = True)
		db_file = normpath (join (db_directory, f"records.json"))
		db = TinyDB (db_file)
		
		db.insert ({
			'paths': the_scan_results ["paths"], 
			'alarms': the_scan_results ["alarms"],
			'stats': the_scan_results ["stats"]
		})
		
		db.close ()

	return {
		"status": the_scan_results,
		
		"paths": the_scan_results ["paths"],
		"alarms": the_scan_results ["alarms"],
		"stats": the_scan_results ["stats"]
	}

	'''
		This runs the script at the "before" path,
		if the "before" path is a string.
		
		"before" is the same structure as regular checks.
	'''
	if (type (before) == str):
		before_path_statuses = turn_on_one (
			before,
			module_paths,
			relative_path,
			records
		)
		print (
			"before path statuses:", 
			json.dumps (before_path_statuses, indent = 4)
		)
		
		assert (before_path_statuses ['stats']['passes'] >= 1)
		assert (before_path_statuses ['stats']['alarms'] == 0)
		

	'''
		This runs the checks either simultenously or sequentially.
	'''
	if (simultaneous == True):
		path_statuses = turn_on_simultaneously (
			finds,
			module_paths,
			relative_path,
			records,
			
			simultaneous_capacity = simultaneous_capacity,
		)
	else:
		path_statuses = turn_on_sequentially (
			finds,
			module_paths,
			relative_path,
			records
		)
	
	
	'''
		This runs the script at the "after" path,
		if the "after" path is a string.
		
		"after" is the same structure as regular checks.
	'''
	if (type (after) == str):
		after_path_statuses = turn_on_one (
			after,
			module_paths,
			relative_path,
			records
		)
		print ("before path statuses:", json.dumps (after_path_statuses, indent = 4))
		
		assert (after_path_statuses ['stats']['passes'] >= 1)
		assert (after_path_statuses ['stats']['alarms'] == 0)


	'''
		This aggregates (or squeezes) the proceeds of the
		scan into one dictionary (JSON).
	'''
	status = aggregate.start (
		path_statuses,
		
		aggregation_format = aggregation_format
	)
	stats = status ["stats"]
	paths = status ["paths"]
	alarms = alarm_parser.start (status ["paths"])	
		
	
	
	'''
		If a db_directory is designated,
		then this adds the proceeds to the DB.
	'''
	if (type (db_directory) == str):
		os.makedirs (db_directory, exist_ok = True)
		db_file = normpath (join (db_directory, f"records.json"))
		db = TinyDB (db_file)
		
		db.insert ({
			'paths': paths, 
			'alarms': alarms,
			'stats': stats
		})
		
		db.close ()
		
	
	if (records >= 1):
		rich.print_json (data = {
			"paths": paths
		})
		
		printout_passes (paths)
		
		rich.print_json (data = {
			"alarms": alarms
		})
		rich.print_json (data = {
			"stats": stats
		})		
		
	return {
		"status": status,
		
		"paths": paths,
		"alarms": alarms,
		"stats": stats
	}
	
