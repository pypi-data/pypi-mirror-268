
'''

'''

import rich

from factory_farm.procedures.implicit_procedure.process.variables import implicit_procedure_variables

from .send_done import send_done
from .aggregate_stats import aggregate_stats


def venture_finish ():
	print ()
	print ("checking if is done")
	print ()
	
	the_internal_statuses = implicit_procedure_variables ["internal_statuses"]

	if (implicit_procedure_variables ["internal_statuses_built"] != "yes"):
		return;
	
	for internal_status in the_internal_statuses:
		rich.print_json (
			data = {
				"internal status": {
					internal_status: the_internal_statuses [internal_status] [ "status" ] 
				}
			}
		)
	
	
		#
		#	if the process is done, then the scan:
		#	
		#		( ) exitted
		#		( ) sent /done_with_scan
		#
		#		( ) unlikely -> neither?
		#
		
		#if (the_internal_statuses [ internal_status ] [ "status" ] [ "scan" ] != "done"):
		#	return "no";
			
		if (the_internal_statuses [ internal_status ] [ "status" ] [ "process" ] != "done"):
			return "no";
		
	'''
		if not bounced, then send done
	'''	
	send_done (
		host = implicit_procedure_variables ["intro_harbor"] ["host"],
		port = implicit_procedure_variables ["intro_harbor"] ["port"],
		
		proceeds = aggregate_stats ()
	)