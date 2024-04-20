#!/usr/bin/python3


'''
	This is called from the open
'''
import json
from os.path import dirname, join, normpath
import os
import pathlib
import sys

import click

from keg import open_harbor

def keg_clique ():
	@click.group ("keg")
	def group ():
		pass

	'''
		./status_check keg open --port 10000
	'''
	@group.command ("open")
	@click.option ('--port', required = True)	
	def open (port):
		open_harbor (
			port = port
		)


	return group
	
def start_clique ():
	@click.group ()
	def group ():
		pass
		
	group.add_command (keg_clique ())
	group ()




#
