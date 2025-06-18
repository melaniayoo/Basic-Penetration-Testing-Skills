import nmap     # Import the python-nmap library to run and parse nmap scans

scanner = nmap.PortScanner()    # Create an instance of the PortScanner class

print("Welcome, this is a simple nmap automation tool.")
print("<---------------------------------------------->")

# Prompt the user for an IP address to scan
ip_addr = input("Please enter the IP address you want to scan: ") 
print("The IP you entered is: ", ip_addr)
type(ip_addr)

# Prompt the user to choose the type of scan
resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

# Case 1: Perform a SYN ACK scan (stealth scan)
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())     # Show nmap version
    scanner.scan(ip_addr, '1-1024', '-v -sS')           # Scan ports 1-1024 using verbose (-v) and SYN scan (-sS)
    print(scanner.scaninfo())                           # Show scan method and port range
    print("IP Status: ", scanner[ip_addr].state())      # Check if host is up or down
    print(scanner[ip_addr].all_protocols())             # List all detected protocols (e.g., tcp)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())# List open TCP ports
# Case 2: Perform a UDP scan
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')           # Scan ports 1-1024 using verbose and UDP scan (-sU)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())# List open UDP ports
# Case 3: Perform a comprehensive scan
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    # Perform a full-featured scan:
    # -v: verbose, -sS: SYN scan, -sV: service version, -sC: default scripts, -A: aggressive, -O: OS detection
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
# Handle invalid input
elif resp >= '4':   
    print("Please enter a valid option.")
