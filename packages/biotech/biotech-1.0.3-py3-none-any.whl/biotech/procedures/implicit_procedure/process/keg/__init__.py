
import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys
import threading
import time


from flask import Flask, request
import rich

from .spaces.done_with_scan import done_with_scan
from .spaces.paths_patch import paths_patch



def open_harbor (
	port = 0,
	records = 0
):
	if (records >= 1):
		print ("opening scan process keg on port:", port)

	#app = Flask (__name__)
	#app = Flask ("implicit procedure harbor")
	app = Flask ("aggregator")


	@app.route ("/", methods = [ 'GET' ])
	def home_get ():	
		return "received"


	@app.route ("/on", methods = [ 'GET' ])
	def on_get ():	
		return "yes"

	
	done_with_scan (app)
	paths_patch (
		app,
		
		implicit_procedure_port = port
	)



	app.run (
		'0.0.0.0',
		port = port,
		debug = False
	)