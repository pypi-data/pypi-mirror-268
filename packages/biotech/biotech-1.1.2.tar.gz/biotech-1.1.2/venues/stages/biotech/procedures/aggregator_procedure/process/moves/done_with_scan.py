

'''
	done_with_scan_move ({
		"path": 
		"result":
	})
'''

'''
	Summary:
		This turns off the scan process.
'''

'''
	Maybe called by:
		global time limit reached.
'''


#----
#
from ..variables import aggregator_variables
from .aggregate_stats import aggregate_stats
#
from biotech.topics.process_on.p_expect.parse_records import parse_p_expect_records
from biotech.topics.show.variable import show_variable
#
#
import rich
#
#
import time
#
#----

def done_with_scan_move (the_packet):
	the_path = the_packet ["path"]
	the_result = the_packet ["result"]
	#the_pid = the_packet ["pid"]
	
	
	show_variable (f'The scan "{ the_path }" sent /done_with_scan.', mode = "condensed")


	#---
	#
	#	Once the status of the scan has been established,
	# 	then the scan process can be stopped.
	#
	aggregator_variables ["internal_statuses"] [ the_path ] ["process"] ["process"].terminate ()
	aggregator_variables ["internal_statuses"] [ the_path ] ["times"] ["ended"] = str (time.time ());
	aggregator_variables ["internal_statuses"] [ the_path ] ["times"] ["elapsed"] = (
		float (aggregator_variables ["internal_statuses"] [ the_path ] ["times"] ["ended"]) - 
		float (aggregator_variables ["internal_statuses"] [ the_path ] ["times"] ["started"])
	);
	aggregator_variables ["internal_statuses"] [ the_path ] ["occurrences"] ["scan process was stopped"] = "yes"
	
	#print ('turning off scan process with pid:', the_pid)
	#os.kill (the_pid, 9)
	#
	#----
	

	
	try:
		aggregator_variables ["internal_statuses"] [ the_path ] ["records"] = parse_p_expect_records (
			records = aggregator_variables ["internal_statuses"] [ the_path ] ["process"] ["records"] (),
			format = "UTF8"
		)
	except Exception:
		show_variable ("The records could not be parsed!")
	
	
	
	'''
		This sets the results packet
	'''
	try:
		the_results_packet = {
			"path": the_path
		}
	
		try:
			the_results_packet ["records"] = aggregator_variables ["internal_statuses"] [ the_path ] ["records"]
		except Exception:
			show_variable ("The records could not be added to the results packet!")
		
		try:
			for result in the_result:
				the_results_packet [ result ] = the_result [ result ]
		except Exception:
			show_variable ("A result in the results could not be added!")
			
		try:
			aggregator_variables ["internal_statuses"] [ the_path ] ["results_of_scan"] = the_results_packet	
		except Exception:
			show_variable ("The results packet could not be added.")
			
	except Exception:
		show_variable ("An exception occurred while building the results.")
	
	
	
	aggregator_variables ["internal_statuses"] [ the_path ] ["occurrences"] ["scan records were retrieved"] = "yes"
	aggregator_variables ["internal_statuses"] [ the_path ] ["times"] ["records retrieval"] = str (time.time ());
	
	time.sleep (1)
	
	'''
		This is only variable that is waited on.
	'''
	aggregator_variables ["internal_statuses"] [ the_path ] ["status"] ["process"] = "done"

