
'''
	This one is used because there is not a
	solid programmatic flask off toggle.
	
		perhaps uvicorn + ... ?
		
		perhaps start the intro in pexpect...
		
			intro 
				aggregator
					health_scan
'''

#----
#
from biotech.topics.show.variable import show_variable
#
#
import rich
#
#
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import time
#
#----

'''
	netstat -tuln | grep 52434
'''


def open_harbor (
	port = 0,
	records = 0,
	
	health_scans_done = lambda *args, **kwargs: None
):
	class RequestHandler (BaseHTTPRequestHandler):
		def do_GET (self):
			self.send_response (200)
			self.send_header ('Content-type', 'text/html')
			self.end_headers ()
			self.wfile.write (b"Hello, World!")

		def do_PATCH (self):
			show_variable ({
				"intro harbor": "@ [patch] /done"
			})	
		
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read (content_length)
			try:
				the_packet = json.loads (post_data.decode('utf-8'))
				
				show_variable ({
					"intro harbor /done: the_packet": the_packet
				})
			
				health_scans_done (the_packet)
				
				self.send_response(200)
			except json.JSONDecodeError:
				self.send_response(400)
				
			self.end_headers()

	class Harbor:
		def __init__(self, host='0.0.0.0', port=5000):
			self.host = host
			self.port = port
			self.httpd = None
			self.Harbor_thread = None

		def start(self):
			show_variable ({
				"starting intro harbor:": {
					"port": self.port,
					"host": self.host
				}
			})
		
			self.httpd = HTTPServer ((self.host, self.port), RequestHandler)
			self.Harbor_thread = threading.Thread(target=self.httpd.serve_forever)
			self.Harbor_thread.start()
			show_variable (f"intro harbor started on {self.host}:{self.port}")

		def stop(self):
			if self.httpd:
				self.httpd.shutdown ()
				self.Harbor_thread.join ()
				show_variable ("intro harbor stopped.")

	harbor = Harbor (
		port = port
	)
	
	
	return [ harbor ]

	#Harbor.stop ()