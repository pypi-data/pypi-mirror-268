

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

#import rich

import sys
for path in sys.path:
	print ("health scan, sys path:", path)

'''
rich.print_json (data = {
	"health scan, sys paths": sys.path
})
'''


def main ():
	status_path = os.environ.get ("factory_farm___status_path")
	status_relative_path = os.environ.get ("factory_farm___status_relative_path")

	host = os.environ.get ("factory_farm___harbor_host")
	port = int (os.environ.get ("factory_farm___harbor_port"))

	proceeds = import_from_path (status_path)

	'''
	rich.print_json (data = {
		"pid": os.getpid (),
		"proceeds": proceeds,
		"harbor": {
			"host": host,
			"port": port
		}
	})
	'''


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