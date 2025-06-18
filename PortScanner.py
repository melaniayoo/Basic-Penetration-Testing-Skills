import socket

# Create a TCP socket using IPv4 addressing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set a timeout of 5 seconds for socket operations (helps avoid indefinite hanging)
s.settimeout(5)

# Prompt user to input the target IP address
host = input("Please enter the IP you want to scan: ")
# Prompt user to input the target port number (converted to integer)
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    # Try to connect to the given host and port
    # connect_ex returns 0 if the connection was successful (port is open), otherwise returns an error code
    if s.connect_ex((host, port)):
        print("The port is closed")
    else: 
        print("The port is open")

portScanner(port)
