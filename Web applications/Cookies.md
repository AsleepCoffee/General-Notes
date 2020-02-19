# Cookies

<details>
<summary>Statlessness and cookies</summary>
<br>
  HTTP is stateless protocol.
  Each request is independent.
  Servers do not keep track.
  
  One of the ways this is solved is with cookies.
  
  <details>
  <summary>Cookies</summary>
  <br>
    - allows server to stores and retrive data from client (browser)
    - stored in browsers temp directories
    - Text only, no executable code
    - Cannot exceed 4K in size
    - Allows for retaining stat with the clients help
      - Session management 
      - User preferences

## REsponse headers:
  
   The server will have the header 
   
              "Set-Cookie <name>=<value>; expires=<date>; domain=<domain>; path=<resource>; secure; httponly"
    
   The client will respond with just use "Cookie: <name>=<value>" when communicating with the server.
  
  **Expire:** When the browser should go and delete and exsponge the cookie. The expiary date that is set on the cookie also determines how the cookie is stored, shorter will go in temp and longer will be held elsewhere.
      A browser with no expirary is a **session cookie** and the remove the cookie when the browser is closed(the only time it may be mentioned is if it were to be retained across browser restarts).In RFC 6265 adds **Max-Age** parameter which is the interval in seconds after receiving the cookie that is should be deleted. 
   
  **Domain:** sub domain where the cookie is valid.
   
  **PATH**  resource(path) where cookie should be sent.
   
  **Secure:** Only sent over HTTPS (cookie will not be sent if talking to the server using HTTP)
  
  **httponly:** Cannot be accessed by Client side scrips directly. Cannot be scripted using Javascript. Is an XSS mitigation technique. 
  
  <details>
  <summary>Session ID</summary>
  <br>
  
  
  </details>
  </details>
</details>
