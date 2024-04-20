


from biotech.topics.process_on.p_expect.implicit import process_on_implicit
from biotech.topics.show.variable import show_variable
from biotech.topics.implicit.thread import implicit_thread
	
#
#
import rich	
from tinydb import TinyDB, Query
import requests
#
#
import atexit
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
	records = 2,
	db_directory = False,
	
	aggregation_format = 1,
	
	relative_path = False,
	module_paths = [],
	
	simultaneous = False,
	simultaneous_capacity = 10,
	
	time_limit = "99999999999999999999999"
):
	bio = on ({
		"glob_string": glob_string,
	
		#
		#	itinerary: optionally dynamic
		#
		"intro_port": intro_port,
		"aggregator_procedure_port": aggregator_procedure_port,
		
		#
		#	0: essentials
		#	1: alarms
		#	2: cautions
		#	3: info
		#	4: info, very detailed
		#
		"records": records,
		"db_directory": db_directory,
		
		"aggregation_format": aggregation_format,
		
		"relative_path": relative_path,
		"module_paths": module_paths,
		
		"simultaneous": simultaneous,
		"simultaneous_capacity": simultaneous_capacity,
		
		"time_limit": time_limit
	})
	
	bio ["off"] ()
	the_report = bio ["proceeds"]
	
	return {
		"status": the_report,
		
		"paths": the_report ["paths"],
		"alarms": the_report ["alarms"],
		"stats": the_report ["stats"]
	}

def on (packet):
	show_variable ({ "intro": "The intro." }, mode = "condensed")

	show_variable ({ 
		"glob_string": packet ["glob_string"] 
	})


	'''
		The other presets are in the
		intro process.
	'''
	if ("intro_port" not in packet):
		packet ["intro_port"] = 52434
	if ("records" not in packet):
		packet ["records"] = 2
	
	
	if ("db_directory" in packet):
		db_directory = packet ["db_directory"]
	else:
		db_directory = None
	
	
	show_variable ("@ intro/on.py", mode = "condensed")
	
	records_level = packet ["records"]

	process_environment = os.environ.copy ()
	process_environment ["PYTHONPATH"] = ":".join ([
		* sys.path
	])
	
	intro_quay_port = str (packet ["intro_port"])
	intro_quay_URL = f"http://0.0.0.0:{ intro_quay_port }"
	
	process_environment ["intro_env_variables"] = json.dumps ({})
	process_environment ["intro_quay_port"] = intro_quay_port
	#process_environment ["records_levels"] = records_level
	
	'''
	show_variable ({
		"@ intro/on.py :: process on implicit": process_environment,
		"proc path:": the_intro_process_path ()
	})
	'''
	
	
	'''
		Make sure the intro harbor is not already on.
	'''
	def check_that_intro_harbor_is_not_on ():
		connected = False
		
		try:
			response = requests.get (
				intro_quay_URL + "/is_on"
			)
			connected = True;
			
		except requests.RequestException as e:
			pass;
			
		if (connected):
			raise Exception ("The intro harbor is already on.")
			
			
	check_that_intro_harbor_is_not_on ()
	
	'''
		If this process exits, the procedure keeps 
		going..
	'''
	the_intro = process_on_implicit (
		"python3 " + the_intro_process_path (),
		
		#CWD = CWD,
		env = process_environment,
		name = "intro"
	)
	
	def at_exit_term ():
		nonlocal the_intro;
		
		try:
			the_intro ["process"].terminate ()
		except Exception as E:
			print ('exit exception:', E)
	
	atexit.register (at_exit_term)
	
	'''
		check that the process is on
	'''
	'''
	while True:
		try:
			print ("checking if is the intro is on on")
			print (the_intro ["process"])
			
			if (the_intro ["process"].is_alive ()):
				print ('on')
			
		except Exception as E:
			print (E)
			pass;
			
		time.sleep (1)
	'''
	
	show_variable ("@ intro/on.py :: after process on implicit", mode = "condensed")	
	
	while True:
		try:
			print ("checking if is the intro harbor on")
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
	

	show_variable ("sending the variables packet", mode = "condensed")
	
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
	
	
	show_variable ("The intro process starter received the_report.", mode = "condensed")
	show_variable ({
		"report": the_report
	})

	#time.sleep (6000000)
	
	if (type (db_directory) == str):
		os.makedirs (db_directory, exist_ok = True)
		db_file = normpath (join (db_directory, f"records.json"))
		db = TinyDB (db_file)
		
		db.insert ({
			'paths': the_report ["paths"], 
			'alarms': the_report ["alarms"],
			'stats': the_report ["stats"]
		})
		
		db.close ()
	
	
	#
	#
	#
	
	barricaded = True;
	the_stop = False;
	def background_task ():
		nonlocal the_stop;
		nonlocal barricaded;

		print ("waiting for off to be called")	

		while the_stop == False:
			time.sleep (.25)
			
		the_intro ["process"].terminate ()
		while barricaded == True:
			print ('waiting for process to exit')
		
			try:
				print ("is_alive:", the_intro ["process"].is_alive ())
			
				if (the_intro ["process"].is_alive () == False):
					barricaded = False
			except Exception as E:
				print ("exception:", E)
				
			time.sleep (.25)
		
	
	background_thread = threading.Thread (target=background_task)
	background_thread.start ()

		
	def turn_off ():
		nonlocal the_stop;
		nonlocal barricaded;
		
		the_stop = True
		
		while barricaded == True:
			print ("barricaded")	
			time.sleep (1)
		
		return;

	return {
		"off": turn_off,
		"proceeds": the_report
	}
