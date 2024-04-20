

import multiprocessing
import time
import threading

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
	#response = requests.get ("http://0.0.0.0:8000/")
	#print (response.text)
	time.sleep (2)
	
	the_proc ["off"] ()
	
	print ("data_1:", data_1.value)

if __name__ == '__main__':
	#freeze_support()
	main ()
	