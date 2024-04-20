




#----
#
from biotech.procedures.aggregator_procedure.process.variables import retrieve_variables
from ..done_with_scan import done_with_scan_move
#
from .records import attach_records
#
from biotech.topics.process_on.p_expect.parse_records import parse_p_expect_records
from biotech.topics.show.variable import show_variable
#
#
from pprint import pprint
import time
import traceback
#
#
import rich
#
#----


'''
	This is run over and over again
	in a loop.
'''
def parse_and_check_is_alive_of_statuses ():
	aggregator_variables = retrieve_variables ()

	records_level = aggregator_variables ["records_level"]

	internal_statuses = aggregator_variables ["internal_statuses"]
	
	'''
	show_variable ({
		"intro variables:": aggregator_variables ["intro_variables"]
	})
	'''
	
	time_limit = aggregator_variables ["intro_variables"] ["time_limit"]

	statuses = {}
	unfinished = []
	for status_path in internal_statuses:
		
		status_of_path = internal_statuses [ status_path ]
		occurrences = status_of_path ["occurrences"]
		
		'''
			This checks if the pexpect 
			process is alive.
		'''
		try:
			if ("process" in internal_statuses [ status_path ] ["process"]):
				if (type (internal_statuses [ status_path ] ["process"] ["process"]) != None):
					alive = internal_statuses [ status_path ] ["process"] ["process"].is_alive ()
					if (alive == True):
						occurrences ["scan process is alive"] = "yes"
					else:
						occurrences ["scan process is alive"] = "no"
				
		except Exception as E:
			print ("process alive check exception:", E)
			#print ("process alive check exception:", traceback.format_exc ())
		
			occurrences ["scan process is alive"] = "unknown"		
		
		
		attach_records (status_path)
		
		
		
		'''
			This stops the process if the
			global time limit was exceeded.
		'''
		try:
			if (
				occurrences ["scan process started"] == "yes" and
				occurrences ["scan process is alive"] == "yes" and
				occurrences ["scan process was stopped"] == "no" and
				len (internal_statuses [ status_path ] ["times"] ["started"]) >= 1
			):			
				if (time.time () - float (internal_statuses [ status_path ] ["times"] ["started"]) >= float (time_limit)):	
				
					try:
						the_scan_records = internal_statuses [ status_path ] ["records"]
					except Exception:
						the_scan_records = "not found"
				
					done_with_scan_move ({
						"path": status_path,
						"result":{
							"alarm": "time limit exceeded",
							"the records": the_scan_records
						}
					})
						
		except Exception as E:
			print ("time limit check exception:", traceback.format_exc ())
			pass;
		

		
		'''
			This checks if the process didn't notify the aggregator within 5 seconds.
		
				scan process venture started == "yes"
				scan process notified aggregator == "no"
				5 seconds elapsed
		'''
		try:
			if (
				occurrences ["scan process venture started"] == "yes" and
				occurrences ["scan process notified aggregator"] == "no"
			):
				elapsed = time.time () - float (internal_statuses [ status_path ] ["times"] ["venture started"]);
				
				show_variable ({
					"elapsed without notification:": elapsed
				})
				
				if (elapsed >= 5):			
					show_variable ({
						"attempting to stop the process": status_path
					})
					
					
					
					aggregator_variables ["internal_statuses"] [ status_path ] ["results_of_scan"] = {
						"path": status_path,
						
						"alarm": "There was most likely an internal problem starting the process.",
						"alarm notes": [
							"After 5 seconds, the process did not notify the aggregator that it had started."
						],
						
						"exited": True
					}
				
					aggregator_variables ["internal_statuses"] [ status_path ] ["status"] ["process"] = "done"
					aggregator_variables ["internal_statuses"] [ status_path ] ["occurrences"] ["done reason give"] = "The process didn't notify the aggregator within 5 seconds."
					
					aggregator_variables ["internal_statuses"] [ status_path ] ["process"] ["process"].terminate ()
					
					show_variable ({
						"process may have stopped": status_path
					})
				
		
		except Exception as E:
			print ("process non-notification exception:", traceback.format_exc ())
			pass;
		
		
		'''
			A live process that is indicating that
			it is infinite loop, when it is not.
			
			Therefore if after 5 seconds the records are
			empty, then therer was mostly likely 
			a problem starting the process.
		
				'scan process venture started': 'yes',
				'scan process started': 'yes',
				'scan process notified aggregator': 'yes',
				'scan process is alive': 'yes',


				'scan process was stopped': 'no',
				'scan returned proceeds': 'no',
				'scan records were retrieved': 'no'
		'''
		try:		
			'''
			show_variable ({
				"doors parsed?": ""
			})
			'''
		
			doors = {
				"1": occurrences ["scan process started"] == "yes",
				"2": occurrences ["scan process is alive"] == "yes",
				"3": occurrences ["scan process was stopped"] == "no",
				"4": len (internal_statuses [ status_path ] ["times"] ["venture started"]) >= 1,
				"6": len (internal_statuses [ status_path ] ["records"]) == 0,
				"7": time.time () - float (internal_statuses [ status_path ] ["times"] ["venture started"])
			}
			
			'''
			show_variable ({
				"doors": doors
			})
			'''
			
		
			if (
				occurrences ["scan process started"] == "yes" and
				occurrences ["scan process is alive"] == "yes" and
				occurrences ["scan process was stopped"] == "no" and
				len (internal_statuses [ status_path ] ["times"] ["venture started"]) >= 1 and
				
				len (internal_statuses [ status_path ] ["records"]) == 0
			):
				elapsed = time.time () - float (internal_statuses [ status_path ] ["times"] ["venture started"]);
				
				show_variable ({
					"elapsed": elapsed
				})
			
				if (elapsed >= 10):			
					show_variable ({
						"records were not retrieved after 10 seconds": status_path
					})
					
					try:
						occurrences = internal_statuses [ status_path ] ["occurences"];
					except Exception:
						occurrences = "not found"
					
					aggregator_variables ["internal_statuses"] [ status_path ] ["results_of_scan"] = {
						"path": status_path,
						
						"alarm": "There was most likely an internal problem starting the process.",
						"alarm notes": [
							"After 10 seconds, no process logs were found."
						],
						
						"occurences": occurrences,
						
						"exited": True
					}
				
					aggregator_variables ["internal_statuses"] [ status_path ] ["status"] ["process"] = "done"
					aggregator_variables ["internal_statuses"] [ status_path ] ["process"] ["process"].terminate ()
					
					
						
		except Exception as E:
			print ("process logs time limit check exception:", E)
			pass;
		
		
		
		'''
			Alarm Possibility: 
				"The process exited before results could be sent."
		
			Description:
				This indicates the process is done,
				if while reading the path an exit occurred.
				
					examples:
						1 / 0
						exit ()
		'''
		try:
			if (
				occurrences ["scan process started"] == "yes" and		
				occurrences ["scan process notified aggregator"] == "yes" and

				occurrences ["scan process was stopped"] == "no" and

				occurrences ["scan process is alive"] != "yes"				
			):		
				aggregator_variables ["internal_statuses"] [ status_path ] ["results_of_scan"] = {
					"path": status_path,
					
					"alarm": "The process exited before results could be sent.",
					"alarm notes": [],
					"occurrences": occurrences,
					
					"exited": True
				}
			
				aggregator_variables ["internal_statuses"] [ status_path ] ["status"] ["process"] = "done"

		except Exception as E:
			print ("parse and check exception:", traceback.format_exc ())
			pass;
		
		
		'''
			objective:
				This stops the process if:
					the process is alive, but unresponsive?
		'''
		
		

		
		'''
			This indicate that the process is done normally
		'''
		try:
			if (
				occurrences ["scan process is alive"] == "no" and

				occurrences ["scan process started"] == "yes" and
				occurrences ["scan process was stopped"] == "yes" and
				occurrences ["scan records were retrieved"] == "yes"
			):				
				aggregator_variables ["internal_statuses"] [ status_path ] ["status"] ["process"] = "done"

		except Exception as E:
			print ("parse and check exception:", traceback.format_exc ())
			pass;
		

	
	for status_path in internal_statuses:
		if (internal_statuses [ status_path ] ["status"] ["process"] != "done"):
			unfinished.append ({
				"path": status_path,
				"internals": aggregator_variables ["internal_statuses"] [ status_path ]
			})
	
		
	return unfinished

