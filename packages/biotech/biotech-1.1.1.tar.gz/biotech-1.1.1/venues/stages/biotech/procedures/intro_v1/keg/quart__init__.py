
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
import asyncio
from quart import Quart

def open_harbor (
	port = 0,
	records = 0,
	
	health_scans_done = lambda *args, **kwargs: None
):
	print ("opening intro harbor on port:", port)

	app = Quart (__name__)

	@app.route ('/')
	async def hello ():
		return 'Hello, World!'

	@app.route ("/done", methods = [ 'PATCH' ])
	async def done_patch ():
		print ("@ [patch] /done")
	
		the_packet = await request.get_json ();
		#the_packet = json.loads (request.data.decode ('utf8'))
		rich.print_json (data = {
			"intro done: the_packet": the_packet
		})
	
		health_scans_done (the_packet)
	
		return "received"

	'''
		app.shutdown()
	'''
	def start ():
		return app.run (
			'0.0.0.0',
			port = port,
			debug = False
		)
		
		#return app;
	
	#stop_event = threading.Event ()
	
	harbor = threading.Thread (target = start)
	harbor.daemon = True  # automatically exit when the main program exits
	#harbor.start ()
	
	
	
	# harbor = Process (target = start)
	
	
	'''
		stop_event.set()

		# Wait for the Flask thread to finish
		harbor.join()
	'''
	return [ harbor ];
	
	#server.terminate()
	#server.join()