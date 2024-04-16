
'''
	from factory_farm.procedures.intro.coms.implicit_procedure.on import await_implicit_procedure_is_on
	await_implicit_procedure_is_on (port = 0)
	
	
	
'''

import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents

import requests

def await_implicit_procedure_is_on (
	port = ""
):
	print ("awaiting the open of the implicit procedure harbor")

	def send (arg):
		print ('	checking is on')
	
		try:
			URL = f"http://0.0.0.0:{ port }/on"
			response = requests.get (URL)
			if (response.status_code == 200 and response.text == "yes"):
				return True;
		except Exception:
			pass;
			
		raise Exception ('not on')


	the_proceeds = cycle_loops.start (
		send, 
		cycle_presents ([ 1 ]),
		#cycle_presents (),
		
		loops = 20,
		delay = 1,
		
		records = 0
	)
	
	#print ("the_proceeds:", the_proceeds)
	
	return the_proceeds
