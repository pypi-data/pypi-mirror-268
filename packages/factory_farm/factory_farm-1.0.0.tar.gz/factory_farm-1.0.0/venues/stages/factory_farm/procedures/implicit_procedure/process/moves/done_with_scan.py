

'''
	This turns off the scan process.
'''

import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
import threading
import time

from flask import Flask, request

import rich


from factory_farm.procedures.implicit_procedure.process.variables import implicit_procedure_variables

from .aggregate_stats import aggregate_stats



def done_with_scan_move (
	the_packet = ""
):
	the_path = the_packet ["path"]
	the_result = the_packet ["result"]
	the_pid = the_packet ["pid"]
	
	'''
		turn off the scan process
	'''
	#print ('turning off scan process with pid:', the_pid)
	#os.kill (the_pid, 9)
	
	#
	#	stopping
	#
	print ("stopping:", implicit_procedure_variables ["internal_statuses"] [ the_path ] ["process"] ["process"])
	
	
	status = {
		"path": the_path,
		** the_result
	}
	#implicit_procedure_variables ["paths_statuses"].append (status)
	
	
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["status"] ["scan"] = "done"
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["results_of_scan"] = status
	
	
	#
	#	Once the status of the scan has been established,
	# 	then the scan process can be stopped.
	#
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["process"] ["process"].terminate ()
	

