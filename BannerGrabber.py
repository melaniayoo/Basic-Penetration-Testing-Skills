import socket  # Import Python's built-in socket library for network communication

def banner(ip, port):
    s = socket.socket()  # Create a new TCP socket
    s.connect((ip, int(port)))  # Connect to the given IP and port (must cast port to int)
    s.settimeout(5)  # Set a timeout of 5 seconds for blocking socket operations
    print(str(s.recv(1024)).strip('b'))  # Receive up to 1024 bytes from the socket and print it after removing 'b' from byte string

def main():
    ip = input("Please enter the IP: ")  # Prompt user for target IP address
    port = str(input("Please enter the port: "))  # Prompt user for target port number
    banner(ip, port)  # Call the banner grabbing function with user input

main()  # Run the script
