
'''
	python3 /biotech/venues/stages/biotech/_status/status.proc.py "topics/help_documentation/**/status_*.py"
'''

import biotech.topics.help_documentation as help_documentation

import requests

import time
from os.path import dirname, join, normpath
import pathlib

def check_1 ():
	this_directory = pathlib.Path (__file__).parent.resolve ()
	
	structures = normpath (join (this_directory, "shares"))
	
	
	the_shares = help_documentation.start ({
		"directory": structures,
		"extension": ".s.HTML",
		"relative path": structures,
		
		"port": 20000
	})
	
	port = the_shares.port;
	
	r = requests.get (f'http://localhost:{ port }')
	assert (r.status_code == 200)

	time.sleep (2)
	
	the_shares.stop ()

	return;
	
	
checks = {
	"check 1": check_1
}