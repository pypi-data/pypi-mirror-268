

'''
	This one is for starting from the shell.
	
		[xonsh] status.proc.py
'''

def add_paths_to_system (paths):
	import pathlib
	from os.path import dirname, join, normpath
	import sys
	
	this_folder = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_folder, path)))

add_paths_to_system ([
	'../../../stages',
	'../../../stages_pip'
])

import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()

structures = normpath (join (this_folder, "../../.."))
biotech_path = str (normpath (join (this_folder, "..")))

biotech_path = str (normpath (join (this_folder, "monitors")))


print ("biotech_path:", biotech_path)

import sys
if (len (sys.argv) >= 2):
	glob_string = biotech_path + '/' + sys.argv [1]
else:
	glob_string = biotech_path + '/**/status_*.py'


import biotech._status.establish as establish_status
establish_status.start (
	glob_string = glob_string
)

#
#
#