

'''
	netstat -tuln | grep 8000
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time
import queue

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b"Hello, world!")

class MyHTTPServer(HTTPServer):
	def __init__(self, server_address, RequestHandlerClass):
		super().__init__(server_address, RequestHandlerClass)
		self.shutdown_event = threading.Event()

	def serve_forever(self):
		while not self.shutdown_event.is_set():
			self.handle_request()

	def shutdown(self):
		print ('shutdown?')
	
		self.shutdown_event.set ()
		self.server_close ()
		
		print ('server_closed?')

def start_server(queue):
	server_address = ('', 8000)
	httpd = MyHTTPServer(server_address, MyServer)
	queue.put (httpd)
	
	print('Starting server...')
	httpd.serve_forever()
	
	print('Server stopped.')
	

def stop_server(httpd):
	print('Stopping server...')
	httpd.shutdown ()

if __name__ == '__main__':
	# Create a queue to store the server instance
	server_queue = queue.Queue ()

	# Start the server in a separate thread
	server_thread = threading.Thread(target=start_server, args=(server_queue,))
	server_thread.start()


	httpd = server_queue.get()
	print ("waiting?", httpd)

	# Wait for some time before stopping the server (for demonstration)
	time.sleep (5)

	# Stop the server
	stop_server(httpd)

	# Wait for the server thread to complete
	server_thread.join ()
