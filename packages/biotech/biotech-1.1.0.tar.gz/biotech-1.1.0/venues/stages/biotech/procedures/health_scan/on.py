
'''
	from biotech.procedures.health_scan.on import turn_on_health_check
	the_health_check = turn_on_health_check (
		the_path,
		
		the_module_directories = [],
		relative_path = "",
		
		aggregator_procedure = {
			"port": "",
			"host": ""
		}
	)
	
	the_health_check ["process"].terminate ()
	
	the_report = the_health_check ["report"]	
'''

#----
#
from .dynamic_port import dynamic_port
#
#
import flask
#
#
import os
import pathlib
from os.path import dirname, join, normpath
import sys
#
#----


def the_health_scan_process_path ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return str (normpath (join (this_folder, "process/health_scan.proc.py")))

def find_builtin_modules ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return [
		str (normpath (join (this_folder, "process/modules"))),
		#str (normpath (join (this_folder, "process/modules_pip")))
	]


'''
	packet = {
		"status_check_path": status_check_path,
		
		"module_paths": module_paths,
		"relative_path": relative_path,
		
		"aggregator_procedure": {
			"port": port
		}
	}
'''
def turn_on_health_check (
	packet = {}
):
	the_path = packet ["status_check_path"]
	
	the_module_directories = packet ["module_paths"]
	relative_path = packet ["relative_path"]
	aggregator_procedure = packet ["aggregator_procedure"]

	env = os.environ.copy ()
	env ["PYTHONPATH"] = ":".join ([
		* the_module_directories,
		
		#
		#	These should actually be reduced... to one module...
		#
		* find_builtin_modules ()		
	])

	
	env ["biotech___status_path"] = the_path
		
	env ["biotech___harbor_host"] = "0.0.0.0"
	env ["biotech___harbor_port"] = str (aggregator_procedure ["port"])	
	
	
	if (type (relative_path) == str and len (relative_path) >= 1):
		name = os.path.relpath (the_path, relative_path)
		env ["biotech___status_relative_path"] = relative_path
	else:
		name = "scan " + the_path
		env ["biotech___status_relative_path"] = ''
	
	
	'''
		dynamic port finder
	'''
	
	the_health_check = dynamic_port (
		process_path = the_health_scan_process_path (),
		
		env = env,
		name = name
	)
	

	return the_health_check