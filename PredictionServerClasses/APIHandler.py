from http.server import HTTPServer

from PredictionServerClasses.MyHttpServer import MyHttpServer


class APIHandler:

    def __init__(self):
        self.server = 'None'

    def start_server(self, port=1234):
        print('starting server...')
        server_address = ('127.0.0.1', port)

        self.server = HTTPServer(server_address, MyHttpServer)

        print('running server...')
        self.server.serve_forever()

