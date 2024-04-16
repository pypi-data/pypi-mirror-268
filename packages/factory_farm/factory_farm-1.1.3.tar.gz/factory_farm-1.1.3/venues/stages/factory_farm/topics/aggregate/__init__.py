
'''
	This function aggregates (or summarizes) the stats from
	all of the checks.
'''
def start (
	path_statuses,
	aggregation_format = 1
):
	if (aggregation_format == 1):
		status = {
			"paths": path_statuses,
			"stats": {
				"alarms": 0,
				"empty": 0,
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
	
		for path in path_statuses:
			if ("empty" in path and path ["empty"] == True):
				status ["stats"] ["empty"] += 1
				continue;
			
			if ("alarm" in path):
				status ["stats"] ["alarms"] += 1
				continue;
			
			status ["stats"] ["checks"] ["passes"] += path ["stats"] ["passes"]
			status ["stats"] ["checks"] ["alarms"] += path ["stats"] ["alarms"]
			

		return status
		
	elif (aggregation_format == 2):
		status = {
			"paths": path_statuses,
			"stats": {
				"paths": {
					"alarms": 0,
					"empty": 0,
				},
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
	
		for path in path_statuses:
			if ("empty" in path and path ["empty"] == True):
				status ["stats"] ["paths"] ["empty"] += 1
				continue;
			
			if ("alarm" in path):
				status ["stats"] ["paths"] ["alarms"] += 1
				continue;
			
			status ["stats"] ["checks"] ["passes"] += path ["stats"] ["passes"]
			status ["stats"] ["checks"] ["alarms"] += path ["stats"] ["alarms"]
		
	
		return status;
	
		
	raise Exception (f"aggregation format '{ aggregation_format }' not accounted for.")
		
		
	