
'''
	from biotech.procedures.intro.coms.aggregator_procedure.send_paths import send_paths_to_aggregator
	send_paths_to_aggregator (
		port = 0,
		packet = {}
	)
'''

import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents

import requests

def send_paths_to_aggregator (
	port = "",
	packet = {}
):
	URL = f"http://0.0.0.0:{ port }/paths"
	response = requests.patch (URL, json = packet)
	if (response.status_code == 200 and response.text == "received"):
		return True;

	raise Exception ("An exception occurred while sending the paths to the implicit procedure.")