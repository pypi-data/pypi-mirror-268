
'''
	passes {
		"modules/status_1.py": [
			"check 1"
		]
	}
'''

'''
	option:
		check 1 @ _status/status_1.py 
		check 2 @ _status/status_1.py 
		the module can be turned on and off @ _status/status_1.py 
'''


import rich

def printout_passes (paths):
	try:
		passes = {}

		for path in paths:
			checks = path ["checks"]
			path_string = path ["path"]

			for check in checks:
				check_name = check ["check"]
				passed = check ["passed"]
				
				if (passed == True):
					if (path_string not in passes):
						passes [ path_string ] = []
						
					passes [ path_string ].append (check_name)
					
		rich.print_json (data = {
			"passes": passes
		})
					
	except Exception as E:
		print ("passes printout exception:", E)

	return;