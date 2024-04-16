

'''

'''

from factory_farm.procedures.implicit_procedure.process.moves.format_path import format_path


'''
	paths_statuses = [{
		"path": path,
		** scan_status
	}]
'''

'''
	the_internal_statuses = {
		"status_2.py": {
			"status": {
				"scan": "pending",
				"process": "pending",
			},
			
			
			
			#
			#	"pending"
			#
			"scan status": "done",
						
			"records": [],
			"venture": process_on
		}
	}
'''
implicit_procedure_variables = {
	"intro_harbor": {
		"host": "0.0.0.0",
		"port": ""
	},
	
	"intro_variables": {},
	
	#
	#	This is the list of statuses
	#
	#"paths_statuses": [],
	
	"details": 1,
	
	#
	#
	#
	"internal_statuses": {},
	"internal_statuses_built": "no"
}

def setup_internal_statuses (
	status_check_paths,
	relative_path
):
	for status_check_path in status_check_paths:		
		implicit_procedure_variables ["internal_statuses"] [ format_path (status_check_path, relative_path) ] = {
			"status": {
				"scan": "pending",
				"process": "pending"
			},
			"process": None,
			"results_of_scan": None
		}
			
			
	return;

def change ():
	return;
	
def retrieve ():
	return implicit_procedure_variables;