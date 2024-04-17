
'''
	from biotech.procedures.intro.coms.implicit_procedure.send_paths import send_paths
	send_paths (
		port = 0,
		packet = {}
	)
'''

import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents

import requests

def send_paths (
	port = "",
	packet = {}
):
	print ("awaiting the open of the implicit procedure harbor")


	URL = f"http://0.0.0.0:{ port }/paths"
	response = requests.patch (URL, json = packet)
	if (response.status_code == 200 and response.text == "received"):
		return True;

	raise Exception ("An exception occurred while sending the paths to the implicit procedure.")