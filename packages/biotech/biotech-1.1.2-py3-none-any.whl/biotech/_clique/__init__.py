

print ('biotech')

import biotech.topics.help_documentation as help_documentation
	
import click	
	
import pathlib
import time
from os.path import dirname, join, normpath

def the_help_procedure (
	port = ""
):
	this_directory = pathlib.Path (__file__).parent.resolve ()
	this_module = str (normpath (join (this_directory, "..")))

	print ("port:", port)

	help_documentation.start ({
		"directory": this_module,
		"extension": ".s.HTML",
		"relative path": this_module,
		
		"port": int (port)
	})
	
	while True:
		time.sleep (1)

def clique ():
	@click.group ()
	def group ():
		pass
		
	@click.command ("help")
	@click.option ('--port', default = "20000")
	def help (port):
		the_help_procedure (port)
		
	@click.command ("internal-status")
	@click.option ('--glob-string', default = "")
	def biotech_biotech (glob_string):

		if (len (glob_string) >= 1):
			import pathlib
			from os.path import dirname, join, normpath
			this_folder = pathlib.Path (__file__).parent.resolve ()

			structures = normpath (join (this_folder, "../../.."))
			monitors = str (normpath (join (this_folder, "..")))
	
			glob_string = monitors + "/" + glob_string
	
		import biotech._status.establish as establish_status
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
			

		import biotech
		biotech.start (
			glob_string = CWD + glob_string,
			simultaneous = simultaneous
		)


	group.add_command (help)	
	
	group.add_command (biotech_biotech)	
	group.add_command (status)
	
	#group.add_command (clique_group ())
	group ()




#
