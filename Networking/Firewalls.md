# Firewalls

Specialized software modules running on a computer or a dedicated network device to filter packes coming in and out of a network. Can work on different layer of the OSI model.

Packet filtering can be for characteristics like src/dest address, src/dest port, protocol by inspecting the header of every packet. They then can 

Allow: pass

drop: drops the packet without diagnostic mssg to the packet source host

deny: does not let the packet pass, but notifies the source host.


# Application level firewall

 Checks all OSI layer 7
 
 Insects actual content of packet. i.e drop peer-to-peer app packet or visting a site.
 
 
# IDS/IPS

Special software used for detecting intrusion attempts or ongoing intrusions.

  HIDS (Host IDS)
     - On a host. Sensors monitor application logs, file system changes and changes to the OS.
  
  NIDS (Network IDS)
     - On the network (NIPS in inband where NIDS can be inband or outofband)
  
  
