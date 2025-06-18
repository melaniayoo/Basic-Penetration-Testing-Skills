# import socket

# # creates socket object
# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # host = '192.168.1.78'
# host = socket.gethostname()
# # port number the server will listen on
# port = 8080

# # Binding to socket
# serversocket.bind((host, port)) # Host will be replaced with IP, if changed and not running on host

# # Starting TCP listener
# # 3 means the server can queue up to 3 connections before refusing new ones
# serversocket.listen(3)

# while True:
#     # Starting the connection
#     clientsocket, address = serversocket.accept()

#     print("received connection from %s " % str(address))

#     message = 'Hello! Thank you for connecting to the server. This is an example of how sockets can be used.' + "\r\n"
#     clientsocket.send(message.encode('ascii'))

#     clientsocket.close()

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'  # Listen on all interfaces
port = 8080       # Use a non-privileged port

serversocket.bind((host, port))
serversocket.listen(3)

print(f"Server listening on {host}:{port}...")

while True:
    clientsocket, address = serversocket.accept()
    print(f"Received connection from {address}")

    message = 'Hello from macOS TCP server!\r\n'
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
