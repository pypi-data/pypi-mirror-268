

'''
	stop_process (
		"house_mix.py",
		status = {
			"alarm": "time limit exceeded"
		}
	)
'''

import time

from factory_farm.procedures.implicit_procedure.process.variables import implicit_procedure_variables

def stop_process (
	the_path,
	status
):
	
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["status"] ["scan"] = "done"
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["results_of_scan"] = {
		"path": the_path,
		** status
	}

	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["times"] ["ended"] = str (time.time ());

	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["times"] ["elapsed"] = (
		float (implicit_procedure_variables ["internal_statuses"] [ the_path ] ["times"] ["ended"]) - 
		float (implicit_procedure_variables ["internal_statuses"] [ the_path ] ["times"] ["started"])
	);
	
	#
	#	Once the status of the scan has been established,
	# 	then the scan process can be stopped.
	#
	implicit_procedure_variables ["internal_statuses"] [ the_path ] ["process"] ["process"].terminate ()