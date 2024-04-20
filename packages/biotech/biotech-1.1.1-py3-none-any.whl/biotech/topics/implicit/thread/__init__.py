

'''
	itinerary:
		[ ] 
'''

'''
	description:
		it is inadvisable to stop threads..?
			https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
'''

'''
	def task (
		stop_event = None
	):		
		while not stop_event.is_set ():
			time.sleep(1)

	from biotech.topics.implicit.thread import implicit_thread
	the_task = implicit_thread (
		task = task
	)
	the_task ['on'] ()
	the_task ['off'] ()
'''

'''
	def implicit_task():
		while True:
			time.sleep (5)
			print ("implicit")
			
	implicit_thread = threading.Thread (target = implicit_task)
	implicit_thread.daemon = True
	implicit_thread.start ()
'''

import threading
import time

def implicit_thread (
	task = None
):
	implicit_thread = None;
	stop_event = threading.Event ()
		
	def on ():
		nonlocal implicit_thread;
	
		implicit_thread = threading.Thread (
			target = task,
			kwargs = {
				'stop_event': stop_event
			}
		)
		implicit_thread.daemon = True
		implicit_thread.start ()
	
	def off ():
		nonlocal implicit_thread;
		nonlocal stop_event;
	
		print ('stopping the process')
	
		stop_event.set ()
		implicit_thread.join ()
			
	return {
		'on': on,
		'off': off
	}