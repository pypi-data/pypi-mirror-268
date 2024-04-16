

'''
	from __coms.done_with_scan import done_with_scan
	done_with_scan ()
'''

import requests


def done_with_scan (
	host = "0.0.0.0",
	URL_path = "/done_with_scan",
	port = "",
	
	path = "",
	proceeds = {}
):
	from .send_patch import send_patch
	send_patch ("0.0.0.0", port, "/done_with_scan", proceeds)

	"""
	URL = f"http://{ host }:{ port }{ URL_path }"
	print (f'''
	
	done with scan:
	
		sending:
			URL: { URL }
	
	
	''')

	

	response = requests.patch (URL, json = proceeds)

	print("Response status code:", response.status_code)
	print("Response content:", response.text)
	"""