import json
from http.server import BaseHTTPRequestHandler

from PredictionServerClasses.RequestsRouter import RequestsRouter


class MyHttpServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.router = None

    def do_POST(self):
        print("in post method")

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        json_data = json.loads(str(post_data)[2:-1])

        router = RequestsRouter()

        handler = router.get_handler(json_data['Method'])
        result = handler.handle_request(json_data['Data'])

        result_dict = {
            'Result': result
        }

        json_result = json.dumps(result_dict)

        #  self._set_headers()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json_result, 'utf-8'))

        print("response_send")


"""
def run(port):
    print('starting server...')
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, MyHttpServer)
    print('running server...')
    httpd.serve_forever()



run(1234)
"""