


import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
import threading
import time


from flask import Flask, request
import rich

from factory_farm.topics.queues.queue_capacity_limiter import queue_capacity_limiter
from factory_farm.procedures.health_scan.on import turn_on_health_check

from factory_farm.procedures.implicit_procedure.process.variables import implicit_procedure_variables, setup_internal_statuses
from factory_farm.procedures.implicit_procedure.process.moves.format_path import format_path



def paths_patch (
	app,
	
	implicit_procedure_port = None
):
	@app.route ("/paths", methods = [ 'PATCH' ])
	def paths_patch ():
		print ("@ [patch] /paths")
	
	
		'''
			{
				"paths": [],

				"relative_path": False,
				"relative_path": "/factory_farm/venues/warehouse/0_example/modules",
				
				module_paths = [],
				
				simultaneous = False,
				simultaneous_capacity = 10,
				
				before = False,
				after = False
			}
		'''	
		the_packet = json.loads (request.data.decode ('utf8'))
		rich.print_json (data = {
			"paths the_packet": the_packet
		})

		#----
		#
		status_check_paths = the_packet ["status_check_paths"]

		module_paths = the_packet ["module_paths"]
		relative_path = the_packet ["relative_path"]

		simultaneous = the_packet ["simultaneous"]
		simultaneous_capacity = the_packet ["simultaneous_capacity"]
		
		before = the_packet ["before"]
		after = the_packet ["after"]
		#
		#----
		
		implicit_procedure_variables ["intro_variables"] = the_packet
		implicit_procedure_variables ["intro_harbor"] = the_packet ["the_intro_harbor"]		
		
		
		
		'''
			This initializes the internal statuses.
		'''
		setup_internal_statuses (
			status_check_paths,
			relative_path
		)
		implicit_procedure_variables ["internal_statuses_built"] = "yes"
		#
		# ----
		
		
		
		def venture (status_check_path):
			start_time = str (time.time ())
		
			the_scan = turn_on_health_check (
				packet = {
					"status_check_path": status_check_path,
					
					"module_paths": module_paths,
					"relative_path": relative_path,
					
					"implicit_procedure": {
						"port": implicit_procedure_port
					}
				}
			)
			
			print ()
			print ("the_scan:", the_scan)
			print ()
			
			#the_scan_processes [ status_check_path ] = the_scan
			implicit_procedure_variables [
				"internal_statuses"
			] [ 
				format_path (status_check_path, relative_path) 
			] [ 
				"process" 
			] = the_scan
		
		
			implicit_procedure_variables [
				"internal_statuses"
			] [ 
				format_path (status_check_path, relative_path) 
			] [
				"times"
			] [
				"started"
			] = start_time
		
			return the_scan;
		
		
		
		if (simultaneous):
			proceeds = queue_capacity_limiter (
				capacity = simultaneous_capacity,
				items = status_check_paths,
				move = venture
			)		
			
			print ("queue_capacity_limiter proceeds:", proceeds)
		
		else:
			for status_check_path in status_check_paths:
				venture (status_check_path)
		
		'''
			concurrency
		'''
	
		return "received"