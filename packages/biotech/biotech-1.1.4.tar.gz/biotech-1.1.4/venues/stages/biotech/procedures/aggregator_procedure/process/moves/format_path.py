

'''

'''

import os

def format_path (sub_path, relative_path):
	if (type (relative_path) == str):
		path = os.path.relpath (sub_path, relative_path)
	else:
		path = sub_path
		
	return path;