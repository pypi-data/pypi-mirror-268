

'''
	steps:
		process is started
		
		
'''




#from __keg import open_scan_harbor

from __import_from_path import import_from_path

from __coms.done_with_scan import done_with_scan
from __mixes.format_rel_path import format_rel_path

import os
import time
from pprint import pprint


import sys
for path in sys.path:
	print ("health scan, sys path:", path)

import traceback
import io
def find_trace (exception : Exception) -> str:
	try:
		file = io.StringIO ()
		traceback.print_exception (exception, file = file)
		
		return file.getvalue ().rstrip ().split ("\n")
	except Exception:
		pass;
		
	return 'An exception occurred while calculating trace.'

def main ():
	#raise Exception ("An exception occurred")
	try:
		status_path = os.environ.get ("factory_farm___status_path")
		status_relative_path = os.environ.get ("factory_farm___status_relative_path")

		host = os.environ.get ("factory_farm___harbor_host")
		port = int (os.environ.get ("factory_farm___harbor_port"))

		proceeds = import_from_path (status_path)

		pprint ({
			"pid": os.getpid (),
			"proceeds": proceeds,
			"harbor": {
				"host": host,
				"port": port
			}
		})
	except Exception as E:
		proceeds = {
			"parsed": False,
			"alarm": "An exception occurred while running the scan.",
			"exception": repr (E),
			"exception trace": find_trace (E)
		}

	done_with_scan (
		host = host,
		port = port,
		
		proceeds = {
			"path": format_rel_path (status_path, status_relative_path),
			"result": proceeds,
			"pid": os.getpid ()
		}
	)

	time.sleep (1)

	exit ()


main ();


#send_post_request (host, port, "/", proceeds)