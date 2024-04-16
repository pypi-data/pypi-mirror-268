

'''
	from __mixes.format_rel_path import format_rel_path
	format_rel_path (sub_path, relative_path)
'''

import os

def format_rel_path (sub_path, relative_path):
	if (type (relative_path) == str and len (relative_path) >= 1):
		path = os.path.relpath (sub_path, relative_path)
	else:
		path = sub_path
		
	return path;