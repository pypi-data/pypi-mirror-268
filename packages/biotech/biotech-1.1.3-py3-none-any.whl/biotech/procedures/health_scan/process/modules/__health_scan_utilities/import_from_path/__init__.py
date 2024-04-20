
'''
	from __import_from_path import import_from_path
'''


from fractions import Fraction
import importlib.util
import io
import json
from pathlib import Path
import sys
import time
from time import sleep
from time import perf_counter
import traceback

def find_trace (exception : Exception) -> str:
	try:
		file = io.StringIO ()
		traceback.print_exception (exception, file = file)
		
		return file.getvalue ().rstrip ().split ("\n")
	except Exception:
		pass;
		
	return 'An exception occurred while calculating trace.'

def import_from_path (module_path):
	path_exception = "";
	
	try:	
		findings = []
		stats = {
			"passes": 0,
			"alarms": 0
		}
		
		module_name = "__main__"
	
		spec = importlib.util.spec_from_file_location (module_name, module_path)
		the_module = importlib.util.module_from_spec (spec)
		proceeds = spec.loader.exec_module (the_module)
		
		print ("proceeds", proceeds)
		print ("checks in module", hasattr (the_module, 'checks'))
		
		
		if (hasattr (the_module, 'checks')):
			checks = the_module.checks
			
			for check in checks:
				try:
					time_start = perf_counter ()
					
					checks [ check ] ()
					
					time_end = perf_counter ()
					time_elapsed = time_end - time_start
					
					findings.append ({
						"check": check,
						"passed": True,
						"elapsed": [ time_elapsed, "seconds" ]
					})
					
					stats ["passes"] += 1
					
				except Exception as E:				
					findings.append ({
						"check": check,
						"passed": False,
						"exception": repr (E),
						"exception trace": find_trace (E)
					})
					
					stats ["alarms"] += 1
					
			return {
				"empty": False,
				"parsed": True,
							
				"stats": stats,			
				"checks": findings
			}
			
		else:
			return {
				"empty": True,
				"parsed": True
			}
			
	except Exception as E:
		path_exception = E;
		
	try:	
		return {
			"parsed": False,
			"alarm": "An exception occurred while importing the path.",
			"exception": repr (path_exception),
			"exception trace": find_trace (path_exception)
		}
	except Exception:
		pass;
		
	return {
		"parsed": False,
		"alarm": "An exception occurred while importing the path.  The exception could not be parsed."
	}