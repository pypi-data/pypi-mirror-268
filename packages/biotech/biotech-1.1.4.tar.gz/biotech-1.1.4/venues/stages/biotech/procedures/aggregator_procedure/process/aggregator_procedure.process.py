
#----
#
from biotech.procedures.aggregator_procedure.process.moves.status_check_monitor import status_check_monitor
from biotech.procedures.aggregator_procedure.process.clique import start_clique
#
#
import rich
#
#
import sys
#
#----

'''
rich.print_json (data = {
	"implicit procedure": {
		"sys paths": sys.path
	}
})
'''

print ('''
	
	
	
		aggregator on
		
	
	
''')


import atexit
import traceback

def exit_handler():
	print ("""
	
	
		aggregator atexit
	
	
	""")
	traceback.print_stack()

atexit.register(exit_handler)

status_check_monitor ()
start_clique ()

'''
	
'''
while True:
	print ('''
	
	
	
		aggregator staying on
		
	
	
	''')
	
	
	time.sleep (1)