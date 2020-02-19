# Cookies

  HTTP is stateless protocol.
  Each request is independent.
  Servers do not keep track.
  
  One of the ways this is solved is with cookies.
  
    - allows server to stores and retrive data from client (browser)
    - stored in browsers temp directories
    - Text only, no executable code
    - Cannot exceed 4K in size
    - Allows for retaining stat with the clients help
      - Session management 
      - User preferences

## Response headers:
  
 The client will use the following header to use the cookie(s) set by the server.
   
     Cookie: <name>=<value> when communicating with the server

The server will have the header 
   
    Set-Cookie <name>=<value>; expires=<date>; domain=<domain>; path=<resource>; secure; httponly

  **Expire:** When the browser should go and delete and exsponge the cookie. The expiary date that is set on the cookie also determines how the cookie is stored, shorter will go in temp and longer will be held elsewhere.
      A browser with no expirary is a **session cookie** and the remove the cookie when the browser is closed(the only time it may be mentioned is if it were to be retained across browser restarts).In RFC 6265 adds **Max-Age** parameter which is the interval in seconds after receiving the cookie that is should be deleted. 
   
  **Domain:** Sets the scope of a cookie. domain/subdomain where the cookie is valid. The domain set will also allow the cookie for all of its sub-domains. If domain is for a specific sub domain, it can be used for everything below it, but not equal or higher. 
  
  If the server does not specify the domain attribute, the browser will use set it as the server domain and set the cookie host-only flag, that means the cookie will be sent only to that precise hostname. i.e no subdomains.
   
  **PATH**  resource(path) where cookie should be sent. Will be sent to the resource and aynthing below it but not equal to or above. I.e path=/the/path  will go to /the/path/sub and /the/path/sub2   but not /the/path2
   
  **Secure:** Only sent over HTTPS (cookie will not be sent if talking to the server using HTTP)
  
  **httponly:** Cannot be accessed by Client side scrips directly. Cannot be scripted using Javascript, Flash, Java and any other non-HTML tech from reasing the cookie. Is an XSS cookie stealing mitigation technique. 
  
  
## Sessions 


   Sessions are transfered as cookies. Once set, the session ID can then be used in subsequent requests. 
   
   Good for enumeration:
   
     Websites running PHP might user PHPSESSID 
     
     JSP websites might user JSESSIONID
     
     However as these names can be changes, this is not set in stone.
  
