import socket
import os
import json
import math
import threading

class Server:
    def __init__(self, socket_path):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket_path = socket_path
    
    def start(self):
        try:
            os.unlink(self._socket_path)
        except FileNotFoundError:
            pass
    
        print('Starting up on {}'.format(self._socket_path))
        self._socket.bind(self._socket_path)
        self._socket.listen(1)
        
        while True:
            connection, client_address = self._socket.accept()
            print('Accepted connection')
            client_thread = threading.Thread(target=self.accepted, args=(connection, ))
            client_thread.start()

    def accepted(self, connection):
        try:
            while True:
                recv_data = connection.recv(1024).decode('utf-8')
                print('Received data: {}'.format(recv_data))
                print('-----------------------------------')
                if recv_data:
                    self.respond(connection, recv_data)
                else:
                    print('No data')
                    break
        finally:
            print('Closing current connection')
            connection.close()
    
    def respond(self, connection, recv_data):
        try:
            response = JsonProcessor.process(json.loads(recv_data))
            connection.sendall(response.encode())
        except Exception as e:
            print('Error occurred: {}'.format(str(e)))
            error_str = { "error": str(e) }
            connection.sendall(json.dumps(error_str).encode())
            
class JsonProcessor:
    processor = {
        "floor": (lambda x: math.floor(x), "int"),
        "nroot": (lambda params: (params[1] ** (1/params[0])), "double"),
        "reverse": (lambda s: s[::-1], "string"),
        "validAnagram": (lambda params: set(params[0]) == set(params[1]), "string"),
        "sort": (lambda strArr: sorted(strArr), "string[]")
    }

    def process(jsondata):
        try:
            method = jsondata["method"]
            params = jsondata["params"]
            param_types = jsondata["param_types"]
            id = jsondata["id"]

            res_method = JsonProcessor.processor[method][0](params)
            res_type = JsonProcessor.processor[method][1]
            response = { "result": res_method, "result_types": res_type, "id": id }
            return json.dumps(response)
        
        except Exception as e:
            print('Error occurred: {}'.format(e))
            response = { "error": str(e) }
            return json.dumps(response)

def main():
    socket_path = './socket_file'
    server = Server(socket_path)
    server.start()

if __name__ == "__main__":
    main()