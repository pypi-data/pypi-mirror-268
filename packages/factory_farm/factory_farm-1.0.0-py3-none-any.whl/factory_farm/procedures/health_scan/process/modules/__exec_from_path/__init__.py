



def ________build_helpers ():
	from fractions import Fraction
	import io
	import json
	import sys
	import time
	from time import sleep
	from time import perf_counter
	import traceback
	
	def find_trace (exception : Exception) -> str:
		try:
			file = io.StringIO ()
			traceback.print_exception (exception, file = file)
			
			return file.getvalue ().rstrip ().split ("\n")
		except Exception:
			pass;
			
		return 'An exception occurred while calculating trace.'



	def build_scan_string (path):
		contents = ''
		with open (path, mode = 'r') as selector:
			contents += selector.read ()
	
		contents += '''
			
try:
	______internal_variables ["checks"] = checks;	
	______internal_variables ["checks found"] = True;
except Exception as E:
	print (E)
	______internal_variables ["checks found"] = False;
			'''

		return contents

	return {
		"build_scan_string": build_scan_string,
		"find_trace": find_trace,
		"perf_counter": perf_counter
	}

_____________helpers = ________build_helpers ()


def exec_from_path (module_path):
	_______variables = {
		"external": {
			"path_e": "",
			"findings": [],
			"stats": {
				"passes": 0,
				"alarms": 0
			}
		}
	}

	try:
		______internal_variables = {}
		
		'''
			This is where the check is run.
		'''
		exec (
			_____________helpers ["build_scan_string"] (module_path), 
			{ 
				'______internal_variables': ______internal_variables,
				'__file__': module_path,
				'__name__': '__main__'
			}
		)
		

		if (______internal_variables ["checks found"] == False):
			return {
				"empty": True,
				"parsed": True
			}

		
		checks = ______internal_variables ['checks']		

		
		for check in checks:
			try:
				time_start = _____________helpers ["perf_counter"] ()
				
				
				'''
					This is where the check is run
				'''
				checks [ check ] ()
				
				time_end = _____________helpers ["perf_counter"] ()
				time_elapsed = time_end - time_start
				
				_______variables ["external"] ["findings"].append ({
					"check": check,
					"passed": True,
					"elapsed": [ time_elapsed, "seconds" ]
				})
				
				_______variables ["external"] ["stats"] ["passes"] += 1
				
			except Exception as E:				
				_______variables ["external"] ["findings"].append ({
					"check": check,
					"passed": False,
					"exception": repr (E),
					"exception trace": _____________helpers ["find_trace"] (E)
				})
				
				_______variables ["external"] ["stats"] ["alarms"] += 1
		
		
		return {
			"empty": False,
			"parsed": True,
						
			"stats": _______variables ["external"] ["stats"],			
			"checks": _______variables ["external"] ["findings"]
		}
		
	except Exception as E:		
		_______variables ["external"] ["path_e"] = E;

	return {
		"parsed": False,
		"alarm": "An exception occurred while scanning the path.",
		"exception": repr (
			_______variables ["external"] ["path_e"]
		),
		"exception trace": _____________helpers ["find_trace"] (
			_______variables ["external"] ["path_e"]
		)
	}	
	