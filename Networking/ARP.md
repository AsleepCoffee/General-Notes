## ARP (Address Resolution Protocol)

Dev to match L3 addresses with L2 addresses inside a broadcast domain.

Two types of packets: ARP request and ARP reply

Devices will have an ARP table that will store the IP-MAC pairs and its TTL.

Steps for device: 

Device A is going to send a packet to device B, first it searches its ARP table for device Bs MAC. If its there it sends it with dst L2 addr of device B. If not, then an ARP req is sent on the LAN (src IP: A src MAC: A dst IP: B dst MAC: broadcast). When the device with that IP gets the packet, it responses with DST MAC: A DST IP: A src IP B src MAC B.











