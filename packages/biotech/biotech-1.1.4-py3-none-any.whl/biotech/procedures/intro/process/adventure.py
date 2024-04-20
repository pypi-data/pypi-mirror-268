
print ('intro.proc.py')


#
#
from biotech.procedures.intro.process.keg import open_harbor
from biotech.procedures.intro.process.variables import intro_variables
#from biotech.procedures.intro.process.moves.adventure import adventure
#
from biotech.topics.printout.passes import printout_passes
from biotech.topics.show.variable import show_variable
#
from biotech.procedures.aggregator_procedure.on import aggregator_procedure_on
#
from biotech.procedures.intro.process.coms.aggregator_procedure.on import await_aggregator_procedure_is_on
from biotech.procedures.intro.process.coms.aggregator_procedure.send_paths import send_paths_to_aggregator
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

'''
	steps:
		* start the harbor
		* get the variable packet
'''
def adventure ():
	wait_until_health_scans_done = threading.Event ()
	the_scan_results = {}
	def health_scans_done (the_packet):
		nonlocal the_scan_results;
		
		the_scan_results = the_packet
	
		show_variable ("health_scans_done, opening the door.", mode = "condensed")
		wait_until_health_scans_done.set ()


	show_variable ("""about to start intro harbor""", mode = "condensed")

	port = os.environ.get ('intro_quay_port')
	harbor = open_harbor (
		port = port,
		health_scans_done = health_scans_done
	)

	show_variable ("""intro harbor started""", mode = "condensed")
	
	while type (intro_variables ["packet"]) != dict:
		print ("waiting for variables")
		time.sleep (.3)
		
		
	#----
	#	variable access
	#
	#----
	glob_string = intro_variables ["packet"].get ("glob_string")
	
	#
	#	itinerary: optionally dynamic
	#
	intro_port = intro_variables ["packet"].get ("intro_port", 52434)
	aggregator_procedure_port = intro_variables ["packet"].get ("aggregator_procedure_port", 52435)
	
	#
	#	0: essentials
	#	1: alarms
	#	2: cautions
	#	3: info
	#
	records = intro_variables ["packet"].get ("records", 3)
	
	db_directory = intro_variables ["packet"].get ("db_directory", False)
	
	relative_path = intro_variables ["packet"].get ("relative_path", False)
	module_paths = intro_variables ["packet"].get ("module_paths", [])

	aggregation_format = intro_variables ["packet"].get ("aggregation_format", 1)
	simultaneous = intro_variables ["packet"].get ("simultaneous", False)
	simultaneous_capacity = intro_variables ["packet"].get ("simultaneous_capacity", 10)

	time_limit = intro_variables ["packet"].get ("time_limit", "99999999999999999999999")
	
	#----
	#	variable modificatiosn
	#
	#----
	finds = glob.glob (glob_string, recursive = True)
	relative_path = str (relative_path)	
	records_level = records;
		
	show_variable ({
		"got the variables:": intro_variables ["packet"],
		"finds": finds
	})

	the_aggregator_procedure = aggregator_procedure_on (	
		port = aggregator_procedure_port,
		packet = {}
	)
	
	
	'''
		check if the aggregator is on
	'''
	await_aggregator_procedure_is_on (
		port = aggregator_procedure_port
	)
	
	if (records_level >= 3):
		show_variable ("the aggregator procedure has started", mode = "condensed")

	
	send_paths_to_aggregator (
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
		show_variable ("paths sent, waiting until the scans are done.", mode = "condensed")
	
	wait_until_health_scans_done.wait ()

	show_variable ("done awaiting the health scans", mode = "condensed")
	
	show_variable ({
		"the_aggregator_procedure after stopped:": the_aggregator_procedure,
		"intro: the_scan_results": the_scan_results 
	}, mode = "show")


	
	





