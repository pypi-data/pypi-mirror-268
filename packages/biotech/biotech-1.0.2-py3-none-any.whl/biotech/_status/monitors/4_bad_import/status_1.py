
'''
	python3 /biotech/venues/stages/biotech/_status/status.proc.py "_status/monitors/4_bad_import/status_1.py"
'''

import biotech

import pathlib
from os.path import dirname, join, normpath

def check_1 ():
	
	this_directory = pathlib.Path (__file__).parent.resolve ()
	stasis = normpath (join (this_directory, "stasis"))

	print ("searching:", stasis)
	
	scan = biotech.start (
		glob_string = stasis + '/**/*health.py',
		relative_path = stasis,
		module_paths = [
			#* FIND_STRUCTURE_paths (),			
			normpath (join (stasis, "MODULES"))
		]
	)
	status = scan ['status']
	paths = status ["paths"]
	
	import json
	print ("UT 4 status found", json.dumps (status ["stats"], indent = 4))
	assert (len (paths) == 1)
			
	assert (status ["stats"]["alarms"] == 1)
	assert (status ["stats"]["empty"] == 0)
	assert (status ["stats"]["checks"]["passes"] == 0)
	assert (status ["stats"]["checks"]["alarms"] == 0)

checks = {
	'check 1': check_1
}