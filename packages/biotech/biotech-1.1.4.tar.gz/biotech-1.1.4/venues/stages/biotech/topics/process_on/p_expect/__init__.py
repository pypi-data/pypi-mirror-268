
'''
	from biotech.topics.process_on.p_expect import process_on

	env = os.environ.copy ()
	env ["PYTHONPATH"] = ":".join (sys.path)
	the_venture = process_on (
		env = env
	)
	
	the_records = venture ["records"] ()
	for obj in the_queue:
		print ("UTF8:", obj ["UTF8"] ["line"], end = '')
'''

import pexpect
import rich

import atexit
import os

from multiprocessing import Process, Queue

def off (venture):
	try:
		print ("""
		
			attemping to stop the tethered venture
		
		""")
		#venture.close ()
		venture.terminate ()
	except Exception as E:
		print ("venture off exception:", E)
	
		pass;

	

def process_on (
	process_string,
	#
	the_queue = None,
	CWD = None,
	env = {},
	
	name = "process",
	
	stop_event = None
):
	print ("process_string:", process_string)
	#print ("the_queue:", the_queue)
	#print ("CWD:", CWD)
	#print ("env:", env)

	if (CWD == None):
		CWD = os.getcwd ()
		
	if (the_queue == None):
		the_queue = Queue ()
		
	report = {
		"journal": []
	}
	p = pexpect.spawn (
		process_string,
		
		cwd = CWD,
		env = env,
		timeout = None,
		
		# encoding='utf-8'
	)
	def awareness_EOF (p):
		while not p.eof ():
		
			line = p.readline ()

			try:
				UTF8_line = line.decode ('UTF8')
				#UTF8_line = line.decode('ascii')				
				#UTF8_line = line;
				
				UTF8_parsed = "yes"
			except Exception:
				UTF8_line = ""
				UTF8_parsed = "no"
				
			try:
				hexadecimal_line = line.hex ()
				hexadecimal_parsed = "yes"
			except Exception:
				hexadecimal_line = ""
				hexadecimal_parsed = "no"
			
			
			line_parsed = {
				"UTF8": {
					"parsed": UTF8_parsed,
					"line": UTF8_line
				},
				"hexadecimal": {
					"parsed": hexadecimal_parsed,
					"line": hexadecimal_line
				}
			};
			
			the_queue.put (line_parsed)
			
			report ["journal"].append (line_parsed)
			
			if (UTF8_parsed == "yes"):
				#print (f'[{ name }:UTF8]', UTF8_line, end = '')
				print (f'[{ name }]', UTF8_line, end = '')
				
			else:
				print ('unparseable UTF8 line')
			
			# rich.print_json (data = line_parsed)

	awareness_EOF (p)
	
	atexit.register (off, p)
	
	print ("pexpect spawn started?")
	
	return {
		"process": p,
		
		"report": report
	}