
'''
	from biotech.procedures.intro.keg import open_harbor
	harbor = open_harbor (
		port = 0
	)
	
	harbor.start ()
	harbor.terminate ()
'''


import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
from multiprocessing import Process
import threading
import time

from flask import Flask, request
import rich


def open_harbor (
	port = 0,
	records = 0,
	
	health_scans_done = lambda *args, **kwargs: None
):
	print ("opening intro harbor on port:", port)

	app = Flask (__name__)

	@app.route ("/", methods = [ 'GET', 'PATCH' ])
	def home_get ():	
		return "?"

	@app.route ("/done", methods = [ 'PATCH' ])
	def done_patch ():
		print ("@ [patch] /done")
	
		the_packet = json.loads (request.data.decode ('utf8'))
		rich.print_json (data = {
			"intro done: the_packet": the_packet
		})
	
		health_scans_done (the_packet)
	
		return "received"

	'''
	
	'''
	def start (stop_event):
		app.run (
			'0.0.0.0',
			port = port,
			debug = False
		)
		
		#return app;
	
	stop_event = threading.Event ()
	harbor = threading.Thread (target = start, args=(stop_event, ))
	harbor.daemon = True  # automatically exit when the main program exits
	#harbor.start ()
	
	
	
	# harbor = Process (target = start)
	
	
	'''
		stop_event.set()

		# Wait for the Flask thread to finish
		harbor.join()
	'''
	return [ harbor, stop_event ];
	
	#server.terminate()
	#server.join()