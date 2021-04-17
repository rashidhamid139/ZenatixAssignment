import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len).decode('utf-8').split("=")[1]

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        value = ["SUCCESS", "ERROR"]
        message = random.choice(value)
        if message == "SUCCESS":
            with open('sensor_value.csv', 'a+') as file:
                file.write(str(datetime.now()) +", " + post_body + "\n")
        else:
            pass
        print(message)
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()