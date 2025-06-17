import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.78'
host = socket.gethostname()

port = 444

clientsocket.connect(('192.168.1.78', port))

# sets the max amount of data the client accepts at once
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

