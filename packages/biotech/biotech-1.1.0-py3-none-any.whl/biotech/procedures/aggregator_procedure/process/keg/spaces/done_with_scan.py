


#----
#
from biotech.procedures.aggregator_procedure.process.moves.done_with_scan import done_with_scan_move
from biotech.topics.show.variable import show_variable
#
#
from flask import Flask, request
import rich
#
#
import json
#
#----

def done_with_scan (app):
	@app.route ("/done_with_scan", methods = [ 'PATCH' ])
	def done_patch ():
		show_variable ({
			"dock": {
				"verb": "patch",
				"path": "/done_with_scan"
			}
		})
	
		the_packet = json.loads (request.data.decode ('utf8'))

		
		show_variable ({
			"done_with_scan: packet": the_packet
		})
		
		done_with_scan_move (
			the_packet = the_packet
		)
	
		return "received"

