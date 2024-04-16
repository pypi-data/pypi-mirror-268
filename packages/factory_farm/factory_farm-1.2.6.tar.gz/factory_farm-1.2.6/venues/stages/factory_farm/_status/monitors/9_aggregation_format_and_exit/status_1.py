
'''
	python3 /factory_farm/venues/stages/factory_farm/_status/status.proc.py "_status/monitors/9_aggregation_format_and_exit/status_1.py"
'''

import pathlib
from os.path import dirname, join, normpath
import factory_farm

def check_1 ():
	
	this_directory = pathlib.Path (__file__).parent.resolve ()
	this_module = str (this_directory)
	the_guarantees = str (normpath (join (this_directory, f"guarantees")))
	
	scan = factory_farm.start (
		glob_string = the_guarantees + "/**/guarantee_*.py",
		
		simultaneous = True,
		simultaneous_capacity = 10,

		module_paths = [
			normpath (join (this_module, "modules")),
			normpath (join (this_module, "modules_pip"))
		],

		relative_path = this_module,
		
		aggregation_format = 2
	)

	assert (scan ["stats"] ["paths"] ["alarms"] == 2), scan ["stats"]
	assert (scan ["stats"] ["paths"] ["empty"] == 0), scan ["stats"]

	assert (scan ["stats"] ["checks"] ["passes"] == 1), scan ["stats"]
	assert (scan ["stats"] ["checks"] ["alarms"] == 1), scan ["stats"]
	
checks = {
	'aggregation format and exit': check_1
}
