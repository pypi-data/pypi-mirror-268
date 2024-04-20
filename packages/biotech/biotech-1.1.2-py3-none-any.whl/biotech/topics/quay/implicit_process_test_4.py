


import multiprocessing
import threading
import time

def worker(stop_event, data):
	data.value = 42

	def exit_check ():
		nonlocal stop_event;
		print ('exit check')
	
		while True:
			print ('exit check loop')
			
			try:
				print ("exit check loop", stop_event.is_set ())
			except Exception as E:
				pritn (E)
			
			'''
			if (stop_event.is_set ()):
				print ("exiting")
				exit ()
			'''
		
			time.sleep (1)
		
	print ("implicit_process_crate main")	
		
	implicit_thread = threading.Thread (target = exit_check)
	implicit_thread.start ()

	

if __name__ == "__main__":
	# Create a multiprocessing context with 'spawn' start method
	ctx = multiprocessing.get_context('spawn')

	# Create a shared value in the context
	data = ctx.Value('i', 0)
	stop_event = multiprocessing.Event ()

	# Create a multiprocessing process
	process = ctx.Process(target=worker, args=(stop_event,data,))
	
	# Start the process
	process.start()

	# Wait for the process to finish
	process.join()

	# Print the value set by the worker process
	print("Value set by worker process:", data.value)
