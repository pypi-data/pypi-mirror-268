'''
	from keg.send.done import send_done
	send_done ()
'''

'''
	Summary:
		?
'''

#
from biotech.topics.show.variable import show_variable
#
#
import rich
#
#
import requests
#

def send_done (
	host = "0.0.0.0",
	URL_path = "/done",
	port = "",
	
	proceeds = {}
):
	URL = f"http://{ host }:{ port }{ URL_path }"
	
	show_variable ("sending /done", mode = "condensed")

	response = requests.patch (URL, json = proceeds)

	show_variable (f"sending /done received response: '{ response.text }'", mode = "condensed")
