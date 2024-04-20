


from biotech.topics.process_on.p_expect.implicit import process_on_implicit
from biotech.topics.show.variable import show_variable
#
#
import rich	
from tinydb import TinyDB, Query
import requests
#
#
import glob
import json
import pathlib
from os.path import dirname, join, normpath
import os
import sys
import threading
import time
#
#

def the_intro_process_path ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return str (normpath (join (this_folder, "process/intro.proc.py")))

def on (packet):
	process_environment = os.environ.copy ()
	process_environment ["PYTHONPATH"] = ":".join ([
		* sys.path
	])
	
	intro_quay_port = "52434"
	intro_quay_URL = f"http://0.0.0.0:{ intro_quay_port }"
	
	process_environment ["intro_quay_port"] = intro_quay_port
	
	the_intro = process_on_implicit (
		"python3 " + the_intro_process_path (),
		
		#CWD = CWD,
		env = process_environment,
		name = "intro"
	)
	
	
	
	while True:
		try:
			print ("checking if is on")
			response = requests.get (
				intro_quay_URL + "/is_on"
			)
			print ("Response body to /is_on:", response.text)
			
			if (response.text == "yes"):
				break;
			
		except Exception as E:
			print (E)
			pass;
			
		time.sleep (1)
	
	print ()
	print ("sending the packet")
	print ()
	
	'''
		objective: send the packet to the intro quay
	'''
	response = requests.patch (
		intro_quay_URL + "/start", 
		json = packet
	)
	assert (response.text == "received"), response.text
	
	
	'''
		objective: poll the quay to check if is done
	'''
	while True:
		try:
			response = requests.get (
				intro_quay_URL + "/is_report_ready"
			)
			print ("/is_report_ready:", response.text)
			if (response.text == "yes"):
				break;
			
		except Exception as E:
			print (E)
			pass;
			
		time.sleep (1)
	
	
	
	response = requests.get (
		intro_quay_URL + "/the_report"
	)
	the_report = json.loads (response.text);
	

	show_variable ({
		"the_report:": the_report
	})

	#time.sleep (6000000)
	
	the_intro ["process"].terminate ()
	print ('quay exited')
	

	return the_report
