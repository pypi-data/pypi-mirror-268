'''
	from keg.send.done import send_done
	send_done ()
'''

import requests


def send_done (
	host = "0.0.0.0",
	URL_path = "/done",
	port = "",
	
	proceeds = {}
):
	URL = f"http://{ host }:{ port }{ URL_path }"
	print ("URL:", URL)

	response = requests.patch (URL, json = proceeds)

	print ("Response status code:", response.status_code)
	print ("Response content:", response.text)