import socket

# Create a new TCP/IP socket using IPv4 addressing
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Option 1: Use hardcoded IP address (local or remote)
# host = '192.168.1.78'

# Option 2: Automatically get the hostname of the local machine
host = socket.gethostname()

# Define the target port to connect to
port = 444  # Make sure this matches the port the server is listening on

# Connect to the server using a specific IP address (manual override)
clientsocket.connect(('192.168.1.78', port))

# # Receive up to 1024 bytes of data from the server
message = clientsocket.recv(1024)

# Close the client socket after receiving the message
clientsocket.close()

# Decode the received bytes into a human-readable string using ASCII encoding
print(message.decode('ascii'))
