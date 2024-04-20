
#----
#
from biotech.procedures.aggregator_procedure.process.variables import retrieve_variables
#
from biotech.topics.process_on.p_expect.parse_records import parse_p_expect_records
from biotech.topics.show.variable import show_variable
#
#
import rich
#
#
from pprint import pprint
import time
import traceback
#
#----

def attach_records (status_path):
	aggregator_variables = retrieve_variables ()

	records_level = aggregator_variables ["records_level"]
	internal_statuses = aggregator_variables ["internal_statuses"]

	status_of_path = internal_statuses [ status_path ]
	occurrences = status_of_path ["occurrences"]

	'''
		records parsing:
		
			Record parsing clears the queue.
	'''
	the_records = "The records could not be retrieved."
	try:
		if (records_level >= 4):
			show_variable (f"attempting to parse pexpect records for: { status_path }")
		
		the_records = internal_statuses [ status_path ] ["process"] ["records"] ()

		if (records_level >= 4):
			show_variable ({
				"records": the_records,
				"the_records length:": len (the_records)
			})
		
	except Exception as E:
		print ("records retrieval exception:", E)
	
	'''
		This attaches the records of 
		pending health scans.
		
		Questions:
			simultaneous modification error possibility: "done_with_scan"
	'''
	try:
		if (
			len (the_records) >= 1 and
		
			occurrences ["scan process started"] == "yes" and
			occurrences ["scan process is alive"] == "yes" and
			occurrences ["scan process was stopped"] == "no"
		):		
			parsed_records = parse_p_expect_records (
				records = the_records,
				format = "UTF8"
			)
		
			internal_statuses [ status_path ] ["records"].extend (parsed_records)
		
	except Exception as E:
		#print ("record attachment check exception:", traceback.format_exc ())
		print ("record attachment check exception:", E)
		pass;