
'''
	python3 /biotech/venues/stages/biotech/_status/status.proc.py "_status/monitors/9_aggregation_format_and_exit/status_1.py"
'''

'''
	netstat -tuln | grep 52435
'''

import pathlib
from os.path import dirname, join, normpath
import biotech

import time
import rich

def check_1 ():
	this_directory = pathlib.Path (__file__).parent.resolve ()
	this_module = str (this_directory)
	the_guarantees = str (normpath (join (this_directory, f"guarantees")))
	
	relative_path = str (normpath (join (this_directory, f"..")))
	
	scan = biotech.on ({
		"glob_string": this_module + "/**/guarantee_*.py",
		
		"simultaneous": True,
		"simultaneous_capacity": 10,

		"module_paths": [
			normpath (join (this_module, "modules")),
			normpath (join (this_module, "modules_pip"))
		],

		"relative_path": relative_path,
		
		"aggregation_format": 2
	})


	#time.sleep (5)


	
	#time.sleep (5)

	assert (scan ["stats"] ["paths"] ["alarms"] == 0), scan ["stats"]
	assert (scan ["stats"] ["paths"] ["empty"] == 0), scan ["stats"]

	assert (scan ["stats"] ["checks"] ["passes"] == 1), scan ["stats"]
	assert (scan ["stats"] ["checks"] ["alarms"] == 0), scan ["stats"]
	
checks = {
	'aggregation format and exit': check_1
}
