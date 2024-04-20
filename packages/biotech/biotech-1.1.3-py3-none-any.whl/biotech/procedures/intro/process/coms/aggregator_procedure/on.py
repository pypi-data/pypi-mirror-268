
'''
	from biotech.procedures.intro.coms.aggregator_procedure.on import await_aggregator_procedure_is_on
	await_aggregator_procedure_is_on (port = 0)
	
	
	
'''

import botanist.cycle.loops as cycle_loops
from botanist.cycle.presents import presents as cycle_presents
from biotech.topics.show.variable import show_variable

import requests

def await_aggregator_procedure_is_on (
	port = ""
):
	show_variable ("awaiting the open of the aggregator harbor", mode = "condensed")

	def send (arg):
		show_variable ('	checking if the aggregator is on', mode = "condensed")
	
		try:
			URL = f"http://0.0.0.0:{ port }/on"
			response = requests.get (URL)
			if (response.status_code == 200 and response.text == "yes"):
				return True;
		except Exception:
			pass;
			
		raise Exception ('not on')


	the_proceeds = cycle_loops.start (
		send, 
		cycle_presents ([ 1 ]),
		#cycle_presents (),
		
		loops = 20,
		delay = 1,
		
		records = 0
	)
	
	return the_proceeds
