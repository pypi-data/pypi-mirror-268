


import click

import time


from .group import clique as clique_group


def the_help_procedure ():
	import pathlib
	from os.path import dirname, join, normpath
	this_directory = pathlib.Path (__file__).parent.resolve ()
	this_module = str (normpath (join (this_directory, "..")))

	import shares
	shares.start ({
		"directory": this_module,
		"extension": ".s.HTML",
		"relative path": this_module
	})
	
	while True:
		time.sleep (1)

def clique ():
	print ("clique")

	
	@click.group ()
	def group ():
		pass

	@click.command ("shares")
	def shares ():
		the_help_procedure ()
		
	@click.command ("help")
	def help ():
		the_help_procedure ()
		
	@click.command ("internal-status")
	@click.option ('--glob-string', default = "")
	def factory_farm_factory_farm (glob_string):

		if (len (glob_string) >= 1):
			import pathlib
			from os.path import dirname, join, normpath
			this_folder = pathlib.Path (__file__).parent.resolve ()

			structures = normpath (join (this_folder, "../../.."))
			monitors = str (normpath (join (this_folder, "..")))
	
			glob_string = monitors + "/" + glob_string
	
		import factory_farm._status.establish as establish_status
		establish_status.start (
			glob_string = glob_string
		)
	

	@click.command ("status")
	@click.option ('--simultaneous', default = "yes")
	@click.option ('--glob-string', default = "/**/status_*.py")
	def status (simultaneous, glob_string):
		import pathlib
		from os.path import dirname, join, normpath
		this_directory = pathlib.Path (__file__).parent.resolve ()
		this_module = str (normpath (join (this_directory, "..")))

		import os
		CWD = os.getcwd ()
		
		if (simultaneous == "yes"):
			simultaneous_bool = True
		elif (simultaneous == "no"):
			simultaneous_bool = False
		else:
			print ("'--simultaneous yes' or '--simultaneous no'")
			exit ()
			

		import factory_farm
		factory_farm.start (
			glob_string = CWD + glob_string,
			simultaneous = simultaneous
		)


	group.add_command (shares)	
	group.add_command (help)	
	
	
	group.add_command (factory_farm_factory_farm)	
	group.add_command (status)
	
	group.add_command (clique_group ())
	group ()




#
