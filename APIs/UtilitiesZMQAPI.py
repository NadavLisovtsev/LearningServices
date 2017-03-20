import zmq
import json

class UtilitiesZMQAPI:

    def __init__(self):
        self._port = '5555'

    def send_request(self, data):
        context = zmq.Context()
    #    print("Connecting to ZMQ server...")
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:" + self._port)

    #    print("Sending request %s …" % data)
        socket.send_string(data)

        #  Get the reply.
        message = socket.recv()
     #   print("Received reply %s [ %s ]" % (data, message))
        return float(message)



    def calcAsymptoticAverage(self, l):
        dataDict = {
            'Method': 'CalcAsymptoticAverage',
            'Data': l
        }
        return self.send_request(json.dumps(dataDict))

    def AddValueToAsymptoticAverage(self, value, average):
        dataDict = {
            'Method': 'CalcAsymptoticAverage',
            'Data': [value, average]
        }
        return self.send_request(json.dumps(dataDict))

