   First version of NetBIOS was dev in 1983 as an API (not as a protocol) that served its purpose in deving client/server apps. Originally not intended to be encapped in TCP or UDP , in 1987 NetBIOS over TCP/IP (NetBT or NBT) was released. This was dev to work where the TCP/IP suite is available and is considered a true protocol as described in RFC 1001 and 1002. 

## NETBIOS (Network Basic Input Output System) is the service that allows Windows systems to share files, folders, and printers amoung machines on a LAN. 
 If not config'd it can leak a lot of info, such as shares, system info, user IDs, more.  
 
 - [NetBIOS history](https://github.com/Kahvi-0/General-Notes/blob/master/Networking/NetBIOS.md)
 
 - How NetBIOS and [NetBIOS over TCP (NBT) work](https://docs.microsoft.com/en-us/previous-versions/tn-archive/bb962072(v=technet.10)?redirectedfrom=MSDN): Main purpose is to allow apps on diff systems communicate with one another over the LAN. Used for sharing printers and files, remote procedure calls (RPC), exchange messages, etc. All of which may reveal info. 
 
 Use ports: UDP 137 name services, UDP 138 for datagram services, and TCP 139 for session services. 
  
<img width="640" alt="Capture" src="https://user-images.githubusercontent.com/46513413/86022287-26128f80-b9f8-11ea-8dfe-5f43460c3e02.PNG">

 **[Name service](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738412(v=ws.10)?redirectedfrom=MSDN)** Same purpose of a DNS record, translates and maps a NetBIOS name to an IP. Name = 16-byte address that IDs a NetBIOS resource on the network and ius dynamically registered when either services or apps start. Names can be registered as unique names or as group names. To locate a resource, a NBT name query is used to resolve the NBT name to an IP addr. The 16 characters of a name: first 15 can be specified by the user which the 16th is used to indicate the resource type (00 to FF).
 Some that are available: 
 
 NetBIOS is alos a protocol that functions at the Session and Transport layer of the OSI. 
 
<img width="1309" alt="Capture" src="https://user-images.githubusercontent.com/46513413/86022897-f617bc00-b9f8-11ea-862f-a94a692c6e0e.PNG">
https://msdn.microsoft.com/en-us/library/cc224454.aspx

 nbtstat -n can show the NetBIOS names on our machine. 
 
 The service that maps NetBIOS names to IP is WINS (Windows Internal Name Service). 
 
 **NetBIOS Datagram Services ** permits the sending of datagram messages to and from a NetBIOS name and broadcast the datagram to all NetBIOS names. The datagram and broadcast methods allow one computer to comm with several other computers at the same time, however are limited in message size. No error detection/ correction using datagram or broadcast methods, however datagram comm allows comm without need for a session to be est. 
 
  **Net BIOS Session Service (NBSS)** Allows two names to est a connection in order to exchange data. For example, when a device creates a file sharing connection the session service is used. Once the session has been est, the two workstation use the SMB. 
  
    Steps are used to est the connection: 
    
     1. The NetBIOS name is resolved to an IP
     2. A TCP connection is est between two devices using port 139
     3. The initiating device sends a NetBIOS session req over the TCP conn.
       a. This includes the NetBIOS name of the app that wants to est the conn and the NetBIOS name to which to connect
     4. If the remote device is listening on that name, there will be a positive response and the session will be est. 
