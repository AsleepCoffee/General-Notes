# Kerberose

![Kerbrose](https://user-images.githubusercontent.com/46513413/74048434-315d1400-49a0-11ea-89c1-4d564d83d963.png)

 - TGT: Allows us to ask for tickets(TGS) to use our account authorization. Recived by sending NTLM hash to DC.
 
 - TGS: Allows us to access a service using this ticket. When asking for it we present out TGT to the domain controller. DC responds with the TGS that has been encrypted with the servers account hash that later the server itself would decrypt it using its own server hash. Note the DC does not know if we have access to that service, just give us the hash for it. We then present the TGS to the server we want to authenticate to and the server would know if we would have access to this service with the account that got the TGS.
 
 - PAC
 
 - Application that we are trying to access has an SPN (service principle name)



Random notes:

DC will contains a hidden account called KRBTGT, which is the account that encrypts all of the other tickets. A golden ticket gives you domain admin credentials to any computer on the network that doesn’t expire.
