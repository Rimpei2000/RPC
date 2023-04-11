import socket
import os

# create a socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = './socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

# bind the socket to a server address
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

# open the socket and listen for a request
sock.listen(1)

def floor(num):
    pass

def nroot(n, x):
    pass

def reverse(input_str):
    return input_str[::-1]

def validAnagram(input_str_1, input_str_2):
    pass

def sort(str_arr):
    pass

while True:
    connection, client_address = sock.accept()

    try:
        data = connection.recv(16)
        data_str = data.decode('utf-8')
        print('Received ' + data_str)

        if data:
            response = 'Processing ' + data_str
            # connection.sendall(response.encode())
        else:
            print('no data from', client_address)
            break
    finally:
        print('Closing current connection')
        connection.close()