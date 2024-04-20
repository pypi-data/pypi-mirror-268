



'''
	from biotech.topics.show.variable import show_variable
	show_variable ()
'''

'''
	{
		"line": 
		"file": 
	}
'''

#----
#
import rich
#
#
import inspect
from pprint import pprint
import sys
#
#----

def show_variable (variable, mode = "rich"):
	# print ('show variable:', variable, mode)

	try:
		'''
		
		#
		#	This might cause an infinite loop with pexpect
		#
		
		frame = inspect.currentframe ().f_back
		print ('frame2:', inspect.getframeinfo (inspect.currentframe ()))
		print ('frame:', frame)
		print ('frame2:', inspect.getframeinfo (frame))
		filename = inspect.getframeinfo (frame).filename
		lineno = inspect.getframeinfo (frame).lineno
		'''
		
		filename = "?"
		lineno = "?"
		
		try:
			raise Exception()
		except:
			exc_info = sys.exc_info ()
			
			try:
				filename = exc_info [2].tb_frame.f_code.co_filename
			except Exception:
				pass;
				
			try:
				lineno = exc_info [2].tb_lineno
			except Exception:
				pass;


		if (mode == "pprint"):
			pprint ({
				"path": filename,
				"line": lineno,
				"variable": variable
			})
			
		elif (mode == "show"):
			rich.print ({
				"path": filename,
				"line": lineno,
				"variable": variable
			})
		
		else:		
			rich.print_json (data = {
				"path": filename,
				"line": lineno,
				"variable": variable
			})
			
	except Exception as E:
		print ("variable printing exception:", E)