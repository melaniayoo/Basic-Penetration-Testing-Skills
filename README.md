# Basic-Penetration-Testing-Skills

This repository contains **four individual mini-projects** focused on network communication using Python and socket programming:

1. **TCP Server & Client**
2. **Nmap Scanner**
3. **Banner Grabber**
4. **Port Scanner**

Each project demonstrates foundational networking concepts such as socket communication, service discovery, and port scanning.


## 🧪 Demo: Port Scanner Output

```bash
$ ping hackthissite.org
PING hackthissite.org (137.74.187.103): 56 data bytes
64 bytes from 137.74.187.103: icmp_seq=0 ttl=48 time=263.500 ms

$ python3 PortScanner.py
Please enter the IP you want to scan: 137.74.187.103
Please enter the port you want to scan: 21
The port is closed

$ python3 PortScanner.py
Please enter the IP you want to scan: 137.74.187.103
Please enter the port you want to scan: 80
The port is open
```

## Credits:

Instructions for building these projects can be found at: 
https://www.freecodecamp.org/learn/information-security/