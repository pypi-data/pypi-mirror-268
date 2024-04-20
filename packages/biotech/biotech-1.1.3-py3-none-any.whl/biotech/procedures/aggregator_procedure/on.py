
'''
	from biotech.procedures.aggregator_procedure.on import aggregator_procedure_on
	aggregator_procedure_on ()
'''

'''
	picks:
		( ) sequentially
		( ) simultaneously
		( ) one
'''



'''
	This script starts the keg process.
'''

#----
#
from botanist.cycle.presents import presents as cycle_presents
import botanist.processes.multiple as multi_proc
import botanist.cycle.loops as cycle_loops
import botanist.ports_v2.available as available_port
#
from biotech.topics.process_on.p_expect import process_on
from biotech.topics.process_on.p_expect.implicit import process_on_implicit
from biotech.topics.show.variable import show_variable
#
from .paths import find_aggregator_procedure_paths
#
#
import pexpect
import rich
#
#
import sys
import json
import os
from fractions import Fraction
import time
#
#----

def aggregator_procedure_on (
	port,
	packet
):
	show_variable ("""aggregator_procedure_on""", mode = "condensed")

	limit_start = 25000
		
	path_of_the_scan_process = find_aggregator_procedure_paths ()
	process_string = (
		f'''python3 { path_of_the_scan_process } keg open --port { port }'''
	)
	
	process_environment = os.environ.copy ()
	process_environment ["PYTHONPATH"] = ":".join ([
		* sys.path
	])

	the_venture = process_on_implicit (
		process_string,
		
		CWD = None,
		env = process_environment,
		name = "aggregator"
	)
	
	time.sleep (1)
	show_variable ({
		'the aggregator procedure:': the_venture
	}, mode = "condensed")

	return the_venture

		

	