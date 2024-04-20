

'''
	This one is for calling
	
		[xonsh] biotech status-internal
'''

'''
	import biotech._status.establish as establish_status
	establish_status.start (
		glob_string = glob_string
	) 
'''

import glob
import pathlib
from os.path import dirname, join, normpath
import os

import rich 

import body_scan



def start (
	glob_string = ''
):
	
	this_folder = pathlib.Path (__file__).parent.resolve ()

	structures = normpath (join (this_folder, "../../.."))
	the_stage = str (normpath (join (this_folder, "..")))
	DB = str (normpath (join (this_folder, "DB")))

	#if (len (glob_string) == 0):
	#	glob_string = the_stage + '/**/status_*.py'
	
	status_paths = glob.glob (glob_string, recursive = True)

	
	# path = str (normpath (join (the_stage, "procedures/health_scan/process/modules_pip/requests/status_codes.py")))
	# status_paths.pop (status_paths.index (path))
	
	status_paths.sort ()
	rich.print_json (
		data = status_paths
	)
	


	scan = body_scan.start (
		paths = status_paths,
		
		simultaneous = False,
		
		module_paths = [
			normpath (join (structures, "stages")),
			normpath (join (structures, "stages_pip"))
		],
		
		relative_path = the_stage,
		
		db_directory = DB
	)
	
	rich.print_json (data = {
		"body scan done": scan ["stats"]
	})
	
	assert (scan ["stats"] ["alarms"] == 0), scan ["stats"]
	assert (scan ["stats"] ["empty"] == 0), scan ["stats"]
	assert (scan ["stats"] ["checks"] ["alarms"] == 0), scan ["stats"]
	
	print ("body scan done?")
	
	
	return scan;
