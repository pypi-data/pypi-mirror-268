

'''
	import biotech.topics.alarm_parser as alarm_parser
'''

import json

def start (paths):
	alarms = []

	for path in paths:
		'''
			"path" level alarms
		'''
		
		if (
			"parsed" in path and 
			path ["parsed"] != True
		):
			alarms.append (path)
		elif ("alarm" in path):
			alarms.append (path)
		else:
			pass

		'''
			"check" level alarms
		'''
		if ("checks" not in path):
			continue;
	
		checks = path ["checks"]
	
		this_path = path ["path"]
		unsuccessful = []
		
		for check in checks:
			if (check ["passed"] == False):
				unsuccessful.append (check)
		
		if (len (unsuccessful) >= 1):
			alarms.append ({
				"path": this_path,
				"checks": unsuccessful
			})
			
	
	
	return alarms


