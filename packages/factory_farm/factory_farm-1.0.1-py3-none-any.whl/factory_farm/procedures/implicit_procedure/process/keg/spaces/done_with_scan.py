
import json

from flask import Flask, request
import rich

from factory_farm.procedures.implicit_procedure.process.moves.done_with_scan import done_with_scan_move

def done_with_scan (app):
	@app.route ("/done_with_scan", methods = [ 'PATCH' ])
	def done_patch ():
		print ("@ [patch] /done_with_scan")
	
		the_packet = json.loads (request.data.decode ('utf8'))
		rich.print_json (data = {
			"done_with_scan the_packet": the_packet
		})
		
		done_with_scan_move (
			the_packet = the_packet
		)
	
		return "received"

