



'''
	aggregate_stats (
		path_statuses
	)
'''

'''
	Summary:
		This aggregates the stats after every scan is done.
'''

'''
	format 1:
		{
			"paths": path_statuses,
			"stats": {
				"alarms": 0,
				"empty": 0,
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
		
	format 2:
		{
			"paths": path_statuses,
			"stats": {
				"paths": {
					"alarms": 0,
					"empty": 0,
				},
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
'''

from biotech.procedures.aggregator_procedure.process.variables import aggregator_variables
import biotech.topics.alarm_parser as alarm_parser

from biotech.topics.show.variable import show_variable

'''
	{
		"path": "../status_1.py",
		"empty": false,
		"parsed": true,
		"stats": {
			"passes": 2,
			"alarms": 1
		},
		"checks": []
	}
'''
'''
	maybe?
		"parsed": "unknown",
		"empty": "unknown",
		"stats": {
			"passes": 2,
			"alarms": 1
		},
		"checks": []
'''
def parse_path_statuses ():
	path_statuses = []

	internal_statuses = aggregator_variables ["internal_statuses"]
	for scan_path in internal_statuses:
		results_of_scan = internal_statuses [ scan_path ] ["results_of_scan"]
		if (results_of_scan == None):
			
			the_packet = {
				"path": scan_path,
				"alarm": "no results"
			}
		
			try:
				the_packet ["occurrences"] = internal_statuses [ scan_path ] ["occurrences"]
			except Exception as E:
				print ("results of scan exception 1:", E)
				show_variable (internal_statuses [ scan_path ], mode = "show")
				
			try:
				the_packet ["records"] = internal_statuses [ scan_path ] ["records"]
			except Exception as E:
				print ("results of scan exception 2:", E)
				show_variable (internal_statuses [ scan_path ], mode = "show")
				
			path_statuses.append (the_packet)
				
			

		else:
			path_statuses.append (results_of_scan)
		
	return path_statuses

'''
	This function aggregates (or summarizes) the stats from
	all of the checks.
'''
def aggregate_stats ():
	path_statuses = parse_path_statuses ()
	alarms = alarm_parser.start (path_statuses)	

	aggregation_format = aggregator_variables ["intro_variables"] ["aggregation_format"];

	if (aggregation_format == 1):
		status = {
			"paths": path_statuses,
			"alarms": alarms,
			"stats": {
				"alarms": 0,
				"empty": 0,
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
	
		for path in path_statuses:
			if ("empty" in path and path ["empty"] == True):
				status ["stats"] ["empty"] += 1
				continue;
			
			if ("alarm" in path):
				status ["stats"] ["alarms"] += 1
				continue;
			
			status ["stats"] ["checks"] ["passes"] += path ["stats"] ["passes"]
			status ["stats"] ["checks"] ["alarms"] += path ["stats"] ["alarms"]
			

		return status
		
	elif (aggregation_format == 2):
		status = {
			"paths": path_statuses,
			"alarms": alarms,
			"stats": {
				"paths": {
					"alarms": 0,
					"empty": 0,
				},
				"checks": {
					"passes": 0,
					"alarms": 0
				}
			}
		}
	
		for path in path_statuses:
			if ("empty" in path and path ["empty"] == True):
				status ["stats"] ["paths"] ["empty"] += 1
				continue;
			
			if ("alarm" in path):
				status ["stats"] ["paths"] ["alarms"] += 1
				continue;
			
			status ["stats"] ["checks"] ["passes"] += path ["stats"] ["passes"]
			status ["stats"] ["checks"] ["alarms"] += path ["stats"] ["alarms"]
		
	
		return status;
	
		
	raise Exception (f"aggregation format '{ aggregation_format }' not accounted for.")
		
		
	