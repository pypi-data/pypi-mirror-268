
'''
	from .paths import find_aggregator_procedure_paths
	the_process_path = find_aggregator_procedure_paths ()
'''


import pathlib
from os.path import dirname, join, normpath

def find_aggregator_procedure_paths ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return str (normpath (join (this_folder, "process/aggregator_procedure.process.py")))
	


