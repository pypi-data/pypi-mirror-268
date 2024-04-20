
#----
#
from biotech.procedures.aggregator_procedure.process.variables import aggregator_variables
#	
from ..send_done import send_done
from ..aggregate_stats import aggregate_stats#
#
#----

def send_done_if_finished (unfinished):
	if (len (unfinished) >= 1):
		return;
		
	'''
		This loop might be redundant.
	'''
	the_internal_statuses = aggregator_variables ["internal_statuses"]
	for internal_status in the_internal_statuses:
	
		#
		#	if the process is done, then the scan:
		#	
		#		( ) exitted
		#		( ) sent /done_with_scan
		#
		#		( ) unlikely -> neither?
		#
		#if (the_internal_statuses [ internal_status ] [ "status" ] [ "scan" ] != "done"):
		#	return;
	
		if (the_internal_statuses [ internal_status ] [ "status" ] [ "process" ] != "done"):
			return;
	

	'''
		if not bounced, then send done
	'''	
	send_done (
		host = aggregator_variables ["intro_harbor"] ["host"],
		port = aggregator_variables ["intro_harbor"] ["port"],
		
		proceeds = aggregate_stats ()
	)
	
	return "sent"