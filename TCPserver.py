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

# Create a TCP socket using IPv4 addressing (AF_INET) and stream-based connection (SOCK_STREAM)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all available interfaces on the machine (0.0.0.0) so that external devices can connect
host = '0.0.0.0'  # This makes the server accessible by its IP address from other machines on the network
port = 8080       # Port the server listens on (must match the client-side)

# Bind the socket to the specified host and port
serversocket.bind((host, port))
# Start listening for incoming connections
# Argument '3' means up to 3 incoming connections can be queued
serversocket.listen(3)

print(f"Server listening on {host}:{port}...")

# Infinite loop to accept and handle incoming connections
while True:
    # Accept a new connection
    clientsocket, address = serversocket.accept()
    print(f"Received connection from {address}")

    # Send a welcome message to the connected client
    message = 'Hello from macOS TCP server!\r\n'
    clientsocket.send(message.encode('ascii'))  # Encode message to bytes before sending
    # Close the connection with this client (one-time communication)
    clientsocket.close()
