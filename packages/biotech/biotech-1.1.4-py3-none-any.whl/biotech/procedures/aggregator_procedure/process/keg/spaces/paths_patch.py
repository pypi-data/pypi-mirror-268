
'''
	description:
		This is what starts the aggregator
'''

#----
#
from biotech.procedures.aggregator_procedure.process.variables import aggregator_variables, setup_internal_statuses
from biotech.procedures.aggregator_procedure.process.moves.format_path import format_path
#
from biotech.topics.show.variable import show_variable
from biotech.topics.queues.queue_capacity_limiter import queue_capacity_limiter
from biotech.procedures.health_scan.on import turn_on_health_check
#
#
from flask import Flask, request
import rich
#
#
import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
import threading
import time
#
#----

def paths_patch (
	app,
	
	aggregator_procedure_port = None
):
	@app.route ("/paths", methods = [ 'PATCH' ])
	def paths_patch ():	
		
		'''
			{
				"paths": [],

				"relative_path": False,
				"relative_path": "/biotech/venues/warehouse/0_example/modules",
				
				module_paths = [],
				
				simultaneous = False,
				simultaneous_capacity = 10,
				
				before = False,
				after = False
			}
		'''	
		show_variable ("/paths received", mode = "condensed")
		the_packet = json.loads (request.data.decode ('utf8'))
		show_variable ("/paths parsed the the_packet", mode = "condensed")

		#----
		#
		status_check_paths = the_packet ["status_check_paths"]

		module_paths = the_packet ["module_paths"]
		relative_path = the_packet ["relative_path"]

		simultaneous = the_packet ["simultaneous"]
		simultaneous_capacity = the_packet ["simultaneous_capacity"]
		
		#before = the_packet ["before"]
		#after = the_packet ["after"]
		#
		#----
		
		aggregator_variables ["intro_variables"] = the_packet
		aggregator_variables ["intro_harbor"] = the_packet ["the_intro_harbor"]		
		
		
		if ("records_level" in the_packet):
			aggregator_variables ["records_level"] = the_packet ["records_level"]		
	
		'''
			This initializes the internal statuses.
		'''
		setup_internal_statuses (
			status_check_paths,
			relative_path
		)
		
		
		
		aggregator_variables ["internal_statuses_built"] = "yes"
		#
		# ----
		
		
		
		def venture (status_check_path):
			rel_path = format_path (status_check_path, relative_path);
		
			aggregator_variables ["internal_statuses"] [ rel_path ] ["occurrences"] ["scan process venture started"] = "yes"
			aggregator_variables ["internal_statuses"] [ rel_path ] ["times"] ["venture started"] = str (time.time ())
		
			start_time = str (time.time ())

			show_variable (f"starting scan '{ status_check_path }'", mode = "condensed")
		
			the_scan = turn_on_health_check (
				packet = {
					"status_check_path": status_check_path,
					
					"module_paths": module_paths,
					"relative_path": relative_path,
					
					"aggregator_procedure": {
						"port": aggregator_procedure_port
					}
				}
			)
			
			aggregator_variables ["internal_statuses"] [ rel_path ] ["process" ] = the_scan
			aggregator_variables ["internal_statuses"] [ rel_path ] ["times"] ["started"] = start_time
			aggregator_variables ["internal_statuses"] [ rel_path ] ["occurrences"] ["scan process started"] = "yes"

			show_variable (f"scan started '{ status_check_path }'", mode = "condensed")


			return the_scan;
		
		
		
		if (simultaneous):
			proceeds = queue_capacity_limiter (
				capacity = simultaneous_capacity,
				items = status_check_paths,
				move = venture
			)		
			
			'''
			show_variable ({
				"queue_capacity_limiter proceeds": proceeds
			}, mode = "show")
			'''
			
		else:
			for status_check_path in status_check_paths:
				venture (status_check_path)
		
	
		return "received"