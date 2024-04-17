



import json
import pathlib
import os
from os.path import dirname, join, normpath
import sys

from flask import Flask, request
import rich

from .start_scan import start_scan

from biotech.topics.queues.queue_capacity_limiter import queue_capacity_limiter

def format_path (find, relative_path):
	if (type (relative_path) == str):
		path = os.path.relpath (find, relative_path)
	else:
		path = find
		
	return;

def open_scan_harbor (
	port = 0,
	records = 0
):
	print ("opening health scan harbor on port:", port)

	app = Flask ("health scan harbor")

	@app.route ("/", methods = [ 'GET' ])
	def home_get ():	
		return "?"


	@app.route ("/on", methods = [ 'GET' ])
	def on_get ():	
		return "yes"

	
	'''
	
	'''
	app.run (
		'0.0.0.0',
		port = port,
		debug = False
	)