DHCP is usually used on routers to dynamically assign or revoke IP addresses to hosts, will also set default gateway. is UDP consists of messages that are mostly sent in broadcast and are visible to the entire broadcast domain. A host entering the domain asks for an IP and will pick the best offer and use that IP.

Steps: 

1. New host connect to the network: It sends a DHCP discovery broadcast packet UDP port 67. The src will be 0.0.0.0.

2. The DHCP server responds with a DCHP offer as a broadcast (IP and MAC) with the field YIADDR (your IP address) is the IP its offering. 
 
3. The client responds with another broadcast (broadcast IP) packet: DHCP request. for the offered address.

DHCP client choose the best offer according to the lease time in the DHCP offer, the longer the better. 

4. The DHCP server that recognizes itself as the winner sends a DHCPACK packet in broadcast. The YIADDR contains the client IP addr while the CHADDR (client ethernet address) contains the client MAC address.








