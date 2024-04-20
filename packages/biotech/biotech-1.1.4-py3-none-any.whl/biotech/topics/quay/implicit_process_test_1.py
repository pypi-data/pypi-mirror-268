

import multiprocessing
import time
import threading

def quay (queue):
	print ("quay")
	
	queue.put ("11")

	return;

def infinite_loop (
	stop_event,
	adventure,
	queue,
	
	record_level = 1
):
	def implicit_task ():
		if (record_level >= 3): print ("implicit task before while loop")
	
		while True:
			if (stop_event.is_set ()):
				if (record_level >= 3): print ("stopping and exitting")
				
				exit ()
		
			if (record_level >= 3): print ("implicit task")
		
			time.sleep (1)
			
			if (record_level >= 3): print ("implicit task after sleep")
			
		if (record_level >= 3): print ("implicit task after while loop")

	implicit_thread = threading.Thread (target = implicit_task)
	#implicit_thread.daemon = True
	implicit_thread.start ()


	if (record_level >= 3): print ("main process procedural adventure")
	adventure (queue)
	
	


'''
	objective:
	
		queue = multiprocessing.Queue ()
		
		def the_process ():
			return;
	
		proc = implicit_process (
			process = the_process
		)
		proc ["on"] ()
		
		
		revenue = proc ["queue"] ()
		
		
		proc ["off"] ()
'''	
def implicit_process (
	process = None
):
	stop_event = multiprocessing.Event ()
	
	def on (stop_event, adventure, queue, record_level = 1):
		def on ():
			if (record_level >= 3): print ("implicit task before while loop")
		
			while True:
				if (stop_event.is_set ()):
					if (record_level >= 3): print ("stopping and exitting")
					
					exit ()
			
				if (record_level >= 3): print ("implicit task")
			
				time.sleep (1)
				
				if (record_level >= 3): print ("implicit task after sleep")
				
			if (record_level >= 3): print ("implicit task after while loop")

		implicit_thread = threading.Thread (target = implicit_task)
		#implicit_thread.daemon = True
		implicit_thread.start ()


		if (record_level >= 3): print ("main process procedural adventure")
		adventure (queue)
		
	def off ():
		return;

	return {
		"on": on,
		"off": off
	}

def main ():
	# Create a stop event
	stop_event = multiprocessing.Event ()
	data = multiprocessing.Value('i', 0)

	revenues = {
		"event 1": "?"
	}
	
	def event_1 (revenue):
		nonlocal revenues;
		print ('event 1 called', revenue)
		
		revenues ["event 1"] = "1"

	queue = multiprocessing.Queue ()
	p = multiprocessing.Process(
		target = infinite_loop, 
		args = (stop_event,quay,queue))
	
	p.start ()

	# Wait for some time (for demonstration)
	time.sleep (2)

	# Set the stop event to signal the process to stop
	stop_event.set()

	print ("here?", queue.get ())

	# Wait for the process to complete
	p.join()


main ()
	