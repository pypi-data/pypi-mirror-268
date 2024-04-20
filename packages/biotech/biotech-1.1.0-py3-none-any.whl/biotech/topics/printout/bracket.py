
'''
	from biotech.topics.show.variable import show_variable
	show_variable ()
'''

'''
	{
		"line": 
		"file": 
	}
'''

import rich

import inspect

def show_variable (variable = ""):
	frame = inspect.currentframe().f_back
	filename = inspect.getframeinfo(frame).filename
	lineno = inspect.getframeinfo(frame).lineno
	#print("File:", filename)
	#print("Line number:", lineno)
	
	rich.print_json (data = {
		"path": filename,
		"line": lineno,
		"variable": variable
	})