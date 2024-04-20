

'''

	This might work:

		from biotech.topics.implicit.proc import implicit_process

		def the_process (_data_1):
			print ("the_process with positionals:", _data_1)
			_data_1.value = 11
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
			time.sleep (2)			
			the_proc ["off"] ()
			
			print ("data_1:", data_1.value)

		if __name__ == '__main__':
			# freeze_support()
			main ()
'''


def implicit_process_crate (
	adventure, 

	stop_event, 
	positionals, 
	
	record_level = 1
):
	print ("implicit_process_crate")

	def exit_check ():
		print ('exit check')
	
		while True:
			print ("exit check loop")
		
			if (stop_event.is_set ()):
				print ("exiting")
				exit ()
				
		
			time.sleep (1)
		
	print ("implicit_process_crate main")	
		
	implicit_thread = threading.Thread (target = exit_check)
	implicit_thread.start ()

	adventure (* positionals)


def implicit_process (
	proc = None,
	positionals = []
):
	variables = {
		"stop_event": multiprocessing.Event (),
		"revenue": multiprocessing.Value ('i', 0),
		"p": None
	}
		
	def on ():
		#ctx = multiprocessing.get_context ('spawn')
		#variables ["p"] = ctx.Process (

		variables ["p"] = multiprocessing.Process (
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