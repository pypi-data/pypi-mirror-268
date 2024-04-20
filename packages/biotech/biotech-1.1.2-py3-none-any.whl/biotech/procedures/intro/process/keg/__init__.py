


'''
	from biotech.procedures.intro.keg import open_harbor
	harbor = open_harbor (
		port = 0
	)
	
	harbor.start ()
	harbor.terminate ()
'''

'''
	netstat -tuln | grep 52434
'''

#----
#
from biotech.procedures.intro.process.variables import intro_variables
from biotech.topics.show.variable import show_variable
#
#
import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
from multiprocessing import Process
import threading
import time
#
#
from flask import Flask, request, jsonify
import rich
#
#----

def open_harbor (
	port = 0,
	records_level = 0,
	health_scans_done = lambda *args, **kwargs: None
):
	print ("opening intro harbor on port:", port)

	if (type (records_level) != int):
		records_level = 0

	app = Flask (__name__)

	the_report = {}
	report_is_ready = False;

	@app.route ("/", methods = [ 'GET', 'PATCH' ])
	def home_get ():	
		return "?"
	
	
	@app.route ("/is_on", methods = [ 'GET', 'PATCH' ])
	def is_on ():	
		return "yes"
	
	'''
		coms with intro
	'''	
	#
	#	for intro to send the variables packet
	#
	@app.route ("/start", methods = [ 'PATCH' ])
	def start ():
		the_packet = json.loads (request.data.decode ('utf8'))
		
		if (records_level >= 4):
			show_variable ({
				"/start: the_packet": the_packet
			})
			
		if (records_level == 3):
			show_variable ("/start was called")
		
		'''
			These variables are waited for in an implicit
			while loop in the intro.proc.py
		'''
		intro_variables ["packet"] = the_packet
		
		#
	
		return "received"
		
	#
	#	for intro to off the server
	#	
	@app.route ("/off", methods = [ 'PATCH' ])
	def off ():
		return "received"
	
		
	#
	#	for intro poller to check if the report is ready
	#
	@app.route ("/is_report_ready", methods = [ 'GET' ])
	def is_done ():
		return intro_variables ["the_report_is_ready"]
		
	
	#
	#	access the report
	#
	@app.route ("/the_report", methods = [ 'GET' ])
	def the_report ():
		return jsonify (intro_variables ["the_report"])
		
	
	'''
		coms with aggregator
	'''	
	#
	#	for the aggregator to send the report
	#
	@app.route ("/done", methods = [ 'PATCH' ])
	def done_patch ():
		show_variable ("intro_harbor got /done", mode = "condensed")
	
		the_packet = json.loads (request.data.decode ('utf8'))
			
		show_variable ("intro_harbor /done, packet parsed", mode = "condensed")
	
		intro_variables ["the_report"] = the_packet
		intro_variables ["the_report_is_ready"] = "yes"
	
	
		'''
			This might stop the intro process or something....
		'''
		#health_scans_done (the_packet)
		
		
	

	
		return "received"
	
	
	'''
	app.run (
		'0.0.0.0',
		port = port,
		debug = False
	)
	'''

	'''
		This starts the harbor implicitly
	'''
	def start (stop_event):
		print ("starting app")
	
		app.run (
			'0.0.0.0',
			port = port,
			debug = False
		)
		
		#return app;
	
	stop_event = threading.Event ()
	harbor = threading.Thread (target = start, args=(stop_event, ))
	harbor.daemon = True  # automatically exit when the main program exits
	
	harbor.start ()
	
	'''
		stop_event.set()

		# Wait for the Flask thread to finish
		harbor.join()
	'''

