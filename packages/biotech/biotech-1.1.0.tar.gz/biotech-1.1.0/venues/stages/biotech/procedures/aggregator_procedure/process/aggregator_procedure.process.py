
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

status_check_monitor ()
start_clique ()