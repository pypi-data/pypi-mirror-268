
'''
	from .paths import find_implicit_procedure_paths
	the_process_path = find_implicit_procedure_paths ()
'''


import pathlib
from os.path import dirname, join, normpath


def find_implicit_procedure_paths ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return str (normpath (join (this_folder, "process/implicit_procedure.process.py")))
	


