
'''
	from .send_patch import send_patch
	send_patch ("0.0.0.0", port, "/done_with_scan", {})
'''

import socket
import json
def send_patch (host, port, path, json_data):
    # Convert JSON data to a string
    json_str = json.dumps(json_data)

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        
        # Send the HTTP request
        request = f"PATCH {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/json\r\nContent-Length: {len(json_str)}\r\n\r\n{json_str}"
        s.sendall(request.encode())

        # Receive the response
        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data

    # Print the response
    print ("response:", response.decode())