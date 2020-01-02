# TLS 
 
  ## Transport Layer Security 
  

### Summary 

 TLS is a cryptographic protocol for s end-to-end communications and successor to SSL. Intended to uphold confidentiality and integrity of messages.
 
 Two layers:
 
 The TLS record protocol provides connection security while the TLS handshake protocol enables the client and server to authenticate each other and to negotiate keys before any data is transmitted. A basic TLS andshake is a multi-step process that involves the client and server sending "hello" messages, exchange keys, cipher message and then a finish message. The multi-step process allows TLS to be flexible enough for different apps to use it as the format and order of exchange can be modified.

### Common uses: 

 - Web applications
 
 - Instant messaging
 
 - Email
 
 - VOIP
 
 # Visual walkthrough of TLS 1.2 session 
 
  https://tls.ulfheim.net/
  
 # Certificates
 
  Certificates facilitate an encrypted connection between a browser and a web server while also authenticating the identity of the website that owns the cert.
  
  This will contain the cipher suite information. 
  
# Cipher suite 

  A cipher suite is a set of algorithms that help secure a network connection that uses TLS/SSL.
   
   An example of a cipher suite name: TLS_RSA_WITH_AES_128_GCM_SHA

  - TLS defines the protocol that this cipher suite is for.
  
  - RSA indicates the key exchange algorithm being used.
  
  - AES_128 indicates the block/stream cipher being used to encrypt the message stream...
  
  - GCM The block cipher mode of operation.
  
  - SHA indicates the hash algorithm which is used to authenticate a message.

 
 # Versions
 
 ## TLS 1.0
 
 ## TLS 1.1
 
 ## TLS 1.2
 
 ## TLS 1.3
 
  A rewrite for the whole prtocol rather than previous "bandaids".
  "added a function called “0-RTT resumption” that enables the client and server to remember if they have communicated before. If prior communications exist, the previous keys can be used, security checks skipped and the client and server can begin communicating immediately. It is believed that some of the bigger tech companies pushed for 0-RTT because they benefit from the faster connections, but there is some concern from security professionals."
