
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
from rich.console import Console
#
#
import inspect
from pprint import pprint
import sys
import traceback
#
#----

def get_file_and_line ():
	filename = "?"
	lineno = "?"
	
	try:
		raise Exception ()
	except:
		exc_info = sys.exc_info ()
		
		exc_type, exc_value, exc_traceback = sys.exc_info ()
		
		#filename = exc_traceback.tb_frame.f_back.f_code.co_filename
        #lineno = exc_traceback.tb_frame.f_back.f_lineno
		
		print ("path:", exc_traceback.tb_frame.f_back.f_code.co_filename)
		print ("line:", exc_traceback.tb_frame.f_back.f_lineno)
		
		
		print ("exc_info [2]:", exc_info [2])
		print ("traceback:", traceback.extract_tb (exc_info [2]))

		# print ("exc_info [2]:", exc_info [2].tb_frame)
		
		try:
			filename = exc_info [2].tb_frame.f_code.co_filename
		except Exception:
			pass;
			
		try:
			lineno = exc_info [2].tb_lineno
		except Exception:
			pass;
			
	return [ filename, lineno ]

def show_variable (variable, mode = "rich"):
	# print ('show variable:', variable, mode)

	try:
		filename = "?"
		lineno = "?"
		try:
			raise Exception ()
		except:
			exc_type, exc_value, exc_traceback = sys.exc_info ()
			
			try:
				filename = exc_traceback.tb_frame.f_back.f_code.co_filename
			except Exception:
				pass;
				
			try:
				lineno = exc_traceback.tb_frame.f_back.f_lineno
			except Exception:
				pass;

		if (mode == "pprint"):
			pprint ({
				"variable": variable,
				"path": filename,
				"line": lineno,
			})
		
		elif (mode == "condensed"):
			console = Console()
			
			with console.capture () as capture:
				console.print (variable, end = "")

			# Get the captured output as a string
			output_string = capture.get()
						
			#output_string = str (console.render (console.print (variable)))
			
			#line = str (lineno)
			#file = str (filename)
			
			print (f"{ filename }:{ lineno }: " + output_string, end = "")
		
		elif (mode == "show"):
			rich.print ({
				"variable": variable,
				"path": filename,
				"line": lineno
			})
		
		else:		
			rich.print_json (data = {
				"variable": variable,
				"path": filename,
				"line": lineno
			})
			
	except Exception as E:
		print ("variable printing exception:", E)