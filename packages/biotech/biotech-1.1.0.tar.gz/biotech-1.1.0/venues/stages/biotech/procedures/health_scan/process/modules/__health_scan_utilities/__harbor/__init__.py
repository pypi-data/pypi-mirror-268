



'''
	
'''


from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import time

import rich


def open_harbor (
	port = 0,
	records = 0
):
	class RequestHandler(BaseHTTPRequestHandler):
		def do_GET(self):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(b"Hello, World!")

		def do_PATCH(self):
			print ("""
				
				intro harbor @ [patch] /done
				
			""")	
		
			content_length = int (self.headers ['Content-Length'])
			post_data = self.rfile.read(content_length)
			try:
				the_packet = json.loads (post_data.decode ('utf-8'))
				
				rich.print_json (data = {
					"received packet": the_packet
				})
				
				self.send_response (200)
			except json.JSONDecodeError:
				self.send_response (400)
				
			self.end_headers()

	class Harbor:
		def __init__(self, host='0.0.0.0', port=5000):
			self.host = host
			self.port = port
			self.httpd = None
			self.Harbor_thread = None

		def start(self):
			self.httpd = HTTPServer ((self.host, self.port), RequestHandler)
			self.Harbor_thread = threading.Thread(target=self.httpd.serve_forever)
			self.Harbor_thread.start()
			print(f"Harbor started on {self.host}:{self.port}")

		def stop(self):
			if self.httpd:
				self.httpd.shutdown()
				self.Harbor_thread.join()
				print("Harbor stopped.")

	harbor = Harbor (
		port = port
	)
	
	
	return [ harbor ]

	#Harbor.stop ()