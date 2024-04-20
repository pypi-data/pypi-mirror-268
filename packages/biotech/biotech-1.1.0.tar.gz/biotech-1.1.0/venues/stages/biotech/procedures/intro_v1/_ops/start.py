
'''
	import pathlib
	from os.path import dirname, join, normpath
	
	this_folder = pathlib.Path (__file__).parent.resolve ()
	search = normpath (join (this_folder, "../.."))

	import biotech
	bio = biotech.start (
		glob_string = search + '/**/*status.py'
	)	
'''


#----
#
#
from biotech.topics.printout.passes import printout_passes
from biotech.topics.show.variable import show_variable
#
from biotech.procedures.aggregator_procedure.on import aggregator_procedure_on
#
from biotech.procedures.intro.keg import open_harbor
from biotech.procedures.intro.coms.aggregator_procedure.on import await_aggregator_procedure_is_on
from biotech.procedures.intro.coms.aggregator_procedure.send_paths import send_paths
#
#
import glob
import json
import pathlib
from os.path import dirname, join, normpath
import os
import threading
import time
#
#
import rich	
from tinydb import TinyDB, Query
#
#----

'''
	
'''
def start (
	glob_string = "",
	
	#
	#	itinerary: optionally dynamic
	#
	intro_port = 52434,
	aggregator_procedure_port = 52435,
	
	#
	#	0: essentials
	#	1: alarms
	#	2: cautions
	#	3: info
	#
	records = 3,
	db_directory = False,
	
	aggregation_format = 1,
	
	relative_path = False,
	module_paths = [],
	
	simultaneous = False,
	simultaneous_capacity = 10,
	
	time_limit = "99999999999999999999999"
):
	finds = glob.glob (glob_string, recursive = True)
	relative_path = str (relative_path)	
	
	records_level = records;
		
	if (records_level >= 3):
		show_variable ({
			"glob_string:": glob_string,
			"finds:": finds,
			"finds count:": len (finds)
		})	


	wait_until_health_scans_done = threading.Event ()
	
	the_scan_results = {}
	
	
	'''
		signal thread exit:
			wait_until_health_scans_done.set ()
			
		check: topics.implicit.thread
	'''
	def health_scans_done (the_packet):
		nonlocal the_scan_results;
		
		the_scan_results = the_packet
	
		print ("health_scans_done ->", the_packet)
		print ("health_scans_done:", wait_until_health_scans_done, wait_until_health_scans_done.is_set ())
		
		wait_until_health_scans_done.set ()
		print ("health_scans_done:", wait_until_health_scans_done, wait_until_health_scans_done.is_set ())

		#print ("await_health_scans_done set")
		#print ()

	[ intro_harbor ] = open_harbor (
		port = intro_port,
		health_scans_done = health_scans_done
	)	
	intro_harbor.start ()

	the_aggregator_procedure = aggregator_procedure_on (	
		port = aggregator_procedure_port,
		packet = {}
	)
	
	#time.sleep (1)
	
	
	'''
		check if the implicit procedure is on
	'''
	await_aggregator_procedure_is_on (
		port = aggregator_procedure_port
	)
	
	if (records_level >= 3):
		show_variable ("the implicit procedure has started")

	
	send_paths (
		port = aggregator_procedure_port,
		packet = {
			"status_check_paths": finds,
			
			"relative_path": relative_path,
			"module_paths": module_paths,
			
			"simultaneous": simultaneous,
			"simultaneous_capacity": simultaneous_capacity,
			
			#"before": before,
			#"after": after,
			
			"aggregation_format": aggregation_format,
			
			"time_limit": time_limit,
			
			"records_level": records_level,
			
			"the_intro_harbor": {
				"port": intro_port,
				"host": "0.0.0.0"
			}
		}
	)	

	if (records_level >= 3):
		show_variable ("paths sent, waiting until the scans are done.")
	
	wait_until_health_scans_done.wait ()

	if (records_level >= 3):
		show_variable ("done awaiting the health scans")
	

	intro_harbor.stop ()
	
	if (records_level >= 3):
		show_variable ("intro harbor: off")
	
	if (records_level >= 3):
		show_variable ({
			"the_aggregator_procedure:": the_aggregator_procedure
		}, mode = "show")
		
	the_aggregator_procedure ["process"].terminate ()
	
	if (records_level >= 3):
		show_variable ({
			"the_aggregator_procedure after stopped:": the_aggregator_procedure,
			"intro: the_scan_results": the_scan_results 
		}, mode = "show")
	
	if (type (db_directory) == str):
		os.makedirs (db_directory, exist_ok = True)
		db_file = normpath (join (db_directory, f"records.json"))
		db = TinyDB (db_file)
		
		db.insert ({
			'paths': the_scan_results ["paths"], 
			'alarms': the_scan_results ["alarms"],
			'stats': the_scan_results ["stats"]
		})
		
		db.close ()

	#
	#	This is for the body_scan tests,
	#	so that the server ports aren't the same.
	#
	
	
	show_variable ({
		"generating the proceeds": os.getpid ()
	})


	return {
		"status": the_scan_results,
		
		"paths": the_scan_results ["paths"],
		"alarms": the_scan_results ["alarms"],
		"stats": the_scan_results ["stats"]
	}
