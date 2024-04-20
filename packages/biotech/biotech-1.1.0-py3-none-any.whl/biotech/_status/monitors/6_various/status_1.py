

'''
	python3 status.proc.py '_status/monitors/UT/6/status_1.py'
'''

import biotech

import rich

import pathlib
from os.path import dirname, join, normpath
import json

def check_1 ():
	

	this_directory = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (this_directory, "stasis"))

	
	scan = biotech.start (
		glob_string = stasis + '/**/*_health.py',
		
		simultaneous = True,
		
		relative_path = stasis,
		module_paths = []
	)
	status = scan ['status']
	paths = status ["paths"]
	
	
	print ("Unit test suite 6 status found:", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 3), paths
			
	assert (status ["stats"]["alarms"] == 1), status ["stats"]
	assert (status ["stats"]["empty"] == 1), status ["stats"]
	assert (status ["stats"]["checks"]["passes"] == 7), status ["stats"]
	assert (status ["stats"]["checks"]["alarms"] == 1), status ["stats"]
	
checks = {
	'check 1': check_1
}