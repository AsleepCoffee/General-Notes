# Notes

Goal of networking is to exchange info between networked computers, which the info is carried by packets. 

Packets are just streams of bit running as electric signals on physical media used for data transmission. Media can be wire for LAN or air for WiFi.
The signals are interpreted as bits that make up the info.

Packets have a header and a payload

Frames are layer 2 packets.

# Application layers (OSI)

Each layer has its own protocol that talk to the one lower or higher to each other (depending if info is being sent or recieved) called encapsulation. 

The idea is that the entire upper protocol packet (application layer for example) is the entire payload for the lower layer (presentation for example), which then adds its own header on top of that and moves it along. When the receiving host finally gets this packet, it performs that OSI model in reverse.

# IP 

IP (internet protocol) is the protocol that runs on the internet layer of the IP suite, also known as TCP/IP.

IP is in charge of delivering datagrams (IP packets are called datagrams) to hosts involved in a communication and uses IP addresses to ID hosts.


# IPv6 notes

IPv4 compatible: 0:0:0:0:0:0:13.1.68.3 or ::13.1.68.3

::1/128 is loopback

::FFFF:0:0/96 are IPv4 mapped addresses

IPv6 addr can be split in half, network and device part.

The first 48 bits are for internnet global addressing. The network part ends with a dedicated 16-bits pace (one hex word) that can be only used for specifying a subnet. 

![1](https://user-images.githubusercontent.com/46513413/74688204-cd5afc80-51a4-11ea-99dc-41d2d2d9ac48.png)

Three addr types: 

  - Global unicast address - Global and reside on the internet
  
  - Unique local - reside on internal networks or VPNs. Internably routed. 
  
  - Link local - reside on internal networks. Not routed


# Routing 

Routing tables are tables that a router looks at when it is deterining what interface to forward a packet out of after looking at its dest header.

The router will look down the table until one matches or else the packet is dropped. A default route can be defined to say that if none other match , send it to this interface.


# Ports

**Well-known** 0-1023  (Assigned by IANA)











