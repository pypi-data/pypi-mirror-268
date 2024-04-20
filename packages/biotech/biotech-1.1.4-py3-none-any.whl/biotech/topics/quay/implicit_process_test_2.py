

import multiprocessing
import time
import threading



'''
	objective:
	
		def the_process (packet):
			revenue = packet ["revenue"]
			
			return;
		
		def main ():
			data_1 = multiprocessing.Value ('i', 0)
		
			the_proc = implicit_process (
				proc = the_process,
				positionals = [
					data_1
				]
			)
			
			the_proc ["on"] ()
			the_proc ["off"] ()
'''	
def implicit_process (
	proc = None,
	positionals = []
):
	variables = {
		"stop_event": multiprocessing.Event (),
		"revenue": multiprocessing.Value ('i', 0),
		"p": None
	}
	
	def implicit_process_crate (
		adventure, 

		stop_event, 
		positionals, 
		
		record_level = 1
	):
		print ("implicit_process_crate")
	
		def exit_check ():
			while True:
				print ("implicit_process_crate loop", stop_event.is_set ())
			
				if (stop_event.is_set ()):
					exit ()
			
				time.sleep (1)
				
		implicit_thread = threading.Thread (target = exit_check)
		implicit_thread.start ()

		adventure (* positionals)
		
	def on ():
		variables ["p"] = multiprocessing.Process(
			target = implicit_process_crate, 
			args = (
				proc,

				variables ["stop_event"],
				positionals
			)
		)
		variables ["p"].start ()
		
	def off ():
		variables ["stop_event"].set()


	return {
		"on": on,
		"off": off
	}

def main ():
	data_1 = multiprocessing.Value ('i', 0)

	def the_process (_data_1):
		print ("the process:", _data_1)
		data_1.value = 11
		return;

	the_proc = implicit_process (
		proc = the_process,
		positionals = [
			data_1
		]
	)
	
	the_proc ["on"] ()
	
	time.sleep (4)
	
	the_proc ["off"] ()
	
	print ("data_1:", data_1.value)


main ()
	