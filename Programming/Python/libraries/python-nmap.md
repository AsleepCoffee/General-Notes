ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap

## Example


import nmap
import sys

target = str(sys.argv[1])
ports = [str(sys.argv[2])]

scan = nmap.PortScanner()

print("\nScanning for",target,"ports",ports)

for ports in ports: 
  portscan = scan.scan(target,str(port))
