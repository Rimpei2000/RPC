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

def main():
    socket_path = './socket_path'
    server = Server(socket_path)
    server.start()

if __name__ == "__main__":
    main()