

'''
	steps:
		process is started
'''
print ('health scan')

#
#
from __health_scan_utilities.coms.done_with_scan import done_with_scan
from __health_scan_utilities.coms.the_health_scan_started import the_health_scan_started
from __health_scan_utilities.format_rel_path import format_rel_path
from __health_scan_utilities.import_from_path import import_from_path
from __health_scan_utilities.show.variable import show_variable
#
#
import io
import json
import os
from pprint import pprint
import sys
import time
import traceback
#
#

#
#	objective, make the sys path 100% declarative
#
# sys.path = os.environ.get ("PYTHONPATH").split (":")
# print ("health scan, sys path:", json.dumps (sys.path, indent = 4))
#

def find_trace (exception : Exception) -> str:
	try:
		file = io.StringIO ()
		traceback.print_exception (exception, file = file)
		
		return file.getvalue ().rstrip ().split ("\n")
	except Exception:
		pass;
		
	return 'An exception occurred while calculating trace.'

def main ():
	#raise Exception ("An exception occurred")
	status_path = os.environ.get ("biotech___status_path")
	status_relative_path = os.environ.get ("biotech___status_relative_path")
	host = os.environ.get ("biotech___harbor_host")
	port = int (os.environ.get ("biotech___harbor_port"))
	
	the_health_scan_started (
		host = host,
		port = port,
		proceeds = {
			"path": format_rel_path (status_path, status_relative_path),
			"status_path": status_path,
			"relative_path": status_relative_path
		}
	)
	
	#
	#	elapsed check
	#
	time.sleep (1)
	
	try:
		#----
		#
		
		#
		#----

		proceeds = import_from_path (status_path)

		show_variable ({
			"pid": os.getpid (),
			"proceeds": proceeds,
			"harbor": {
				"host": host,
				"port": port
			}
		})
	except Exception as E:
		proceeds = {
			"parsed": False,
			"alarm": "An exception occurred while running the scan.",
			"exception": repr (E),
			"exception trace": find_trace (E)
		}

	done_with_scan (
		host = host,
		port = port,
		
		proceeds = {
			"path": format_rel_path (status_path, status_relative_path),
			"result": proceeds,
			"pid": os.getpid ()
		}
	)

	time.sleep (1)

	exit ()


main ();


#send_post_request (host, port, "/", proceeds)