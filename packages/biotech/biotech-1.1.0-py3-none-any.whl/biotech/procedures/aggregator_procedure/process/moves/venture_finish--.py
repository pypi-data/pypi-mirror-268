
'''

'''



#----
#
from biotech.procedures.aggregator_procedure.process.variables import aggregator_variables
from biotech.topics.show.variable import show_variable
#
from .send_done import send_done
from .aggregate_stats import aggregate_stats
#
#
import rich
#
#----


def venture_finish ():
	show_variable ("checking if is done")

	
	the_internal_statuses = aggregator_variables ["internal_statuses"]

	if (aggregator_variables ["internal_statuses_built"] != "yes"):
		return;
	
	for internal_status in the_internal_statuses:
		show_variable ({
			"internal status": {
				internal_status: the_internal_statuses [internal_status] [ "status" ] 
			}
		})
	
	
		#
		#	if the process is done, then the scan:
		#	
		#		( ) exitted
		#		( ) sent /done_with_scan
		#
		#		( ) unlikely -> neither?
		#
		
		#if (the_internal_statuses [ internal_status ] [ "status" ] [ "scan" ] != "done"):
		#	return "no";
			
		if (the_internal_statuses [ internal_status ] [ "status" ] [ "process" ] != "done"):
			return "no";
		
	'''
		if not bounced, then send done
	'''	
	send_done (
		host = aggregator_variables ["intro_harbor"] ["host"],
		port = aggregator_variables ["intro_harbor"] ["port"],
		
		proceeds = aggregate_stats ()
	)