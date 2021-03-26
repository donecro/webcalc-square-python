# -*- coding:utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from calc import do_calc

Host = '127.0.0.1'
Port = 8006

result = {'error': False, 'string': '', 'answer': ''}


class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        i1 = self.path
        if i1 != '/favicon.ico':
            x = i1[i1.find('x=') + 2:i1.find('&')]
            y = i1[i1.find('y=') + 2:]
            answer = do_calc(x, y)
            result['string'] = x + '^' + y + '=' + str(answer)
            result['answer'] = answer
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())


if __name__ == '__main__':
    server = HTTPServer((Host, Port), Request)
    print("Square: Starting server, listen at: http://%s:%s" % (Host, Port))
    server.serve_forever()
