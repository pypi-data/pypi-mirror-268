
'''

'''

def check_1 ():
	import pathlib
	from os.path import dirname, join, normpath

	this_folder = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (this_folder, f"stasis"))
	variable = normpath (join (this_folder, f"variable"))

	import factory_farm.procedures.data_nodes.tiny as factory_farm_db
	records_1 = factory_farm_db.records (
		db_directory = normpath (join (variable, f"status_db"))
	)

	import factory_farm
	scan = factory_farm.start (
		glob_string = stasis + '/**/guarantee_*.py',
		simultaneous = True,
		relative_path = stasis,
		module_paths = [
			normpath (join (stasis, "modules"))
		],
		db_directory = normpath (join (variable, f"status_db"))
	)
	status = scan ["status"]
	paths = status ["paths"]
	
	'''
	import json
	print (
		f"Unit test suite { ut_number } status found:", 
		json.dumps (status ["stats"], indent = 4)
	)
	'''
	
	assert (len (paths) == 1)
	
	def check_status (status):
		assert (status ["stats"]["alarms"] == 0)
		assert (status ["stats"]["empty"] == 0)
		assert (status ["stats"]["checks"]["passes"] == 1)
		assert (status ["stats"]["checks"]["alarms"] == 0)

	
	check_status (scan ["status"])

	records_2 = factory_farm_db.records (
		db_directory = normpath (join (variable, f"status_db"))
	)
	assert (len (records_2) == (len (records_1) + 1))
	
	last_record = factory_farm_db.last_record (
		db_directory = normpath (join (variable, f"status_db"))
	)
	check_status (last_record)
	
checks = {
	'tinyDB database can be utilized': check_1
}