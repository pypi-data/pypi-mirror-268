

'''
	objectives:
	
		[ ] /aggregator/records
		
		[ ] /health_scans/paths
		
		[ ] /health_scan/{ path }		
'''

#----
#
from .spaces.done_with_scan import done_with_scan
from .spaces.paths_patch import paths_patch
from .spaces.the_health_scan_started import the_health_scan_started
#
from biotech.procedures.aggregator_procedure.process.variables import retrieve_aggregator_variables
#
#
from flask import Flask, request, jsonify
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

def open_harbor (
	port = 0,
	records = 0
):
	if (records >= 1):
		print ("opening scan process keg on port:", port)

	#app = Flask (__name__)
	#app = Flask ("implicit procedure harbor")
	app = Flask ("aggregator harbor")

	'''
		This is what starts the aggregator
	'''
	paths_patch (app, aggregator_procedure_port = port)

	@app.route ("/", methods = [ 'GET' ])
	def home_get ():	
		return jsonify ({
			'/health_scan/<path:health_scan_path>': [ "get" ],
			'/health_scans/paths': [ "get" ],
			'/on': [ "get" ]
		})


	@app.route ("/on", methods = [ 'GET' ])
	def on_get ():	
		return "yes"

		
	@app.route ('/health_scans/paths', methods = [ 'GET' ])
	def on__get__health_scans__paths ():	
		aggregator_variables = retrieve_aggregator_variables ()
		
		the_paths = {}
		
		for path in aggregator_variables ["internal_statuses"]:
			the_paths [ path ] = ""
	
		return jsonify (the_paths)
		
	@app.route ('/health_scan/<path:health_scan_path>', methods = [ 'GET' ])
	def on__get__health_scan__path (health_scan_path):	
		return "yes"
	
	
	the_health_scan_started (app)
	
	done_with_scan (app)
	
	

	app.run (
		'0.0.0.0',
		port = port,
		debug = False
	)