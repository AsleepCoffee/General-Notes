## HTTP (hyper text transfer protocol)

- Layer 7 protocol 

- client to server based architecture

- Request to Response model to server Resources

- Resources are identified by URI/URL

<details>
<summary>The two versions of HTTP</summary>
<br>
   
   Example request: GET / HTTP/1.1
   
   1.0:
        - One TCP connection per resource and disconnect as soon as its done.

   1.1:
        - Can reuse same TCP connection and request multiple URIs.
        - When you make a request to a sites home page / for example, and it sees refernces to other web elements such as js or css, it will then make more requests for those elements over the same connection.

</details>

<details>
<summary>HTTP request break down</summary>
<br>
----------------------------------------------------------------------
### HTTP response codes:

1xx - Information

2xx - OK

3xx - Redirect

4xx - Bad client request (bad req or not authorized)

5xx - Issue on the server side

### Request methods

GET

POST

## Host header

Tells the server what hostname we are interested in in relation to the page we are requesting.
This is for servers hosting multiple domains.

example you want to go to example.ca but actually want the server my.server
The request to example.ca should look like

      Get / http/1.1
      Host:my.server

## User agent

Details on the users device that is making the request.



When you make basic a request to www.example.ca, you are making a GET request for / of example.ca.

You will see details such the request method, the HTTP response code, and other detials related to the request and response with the HTTP server.

----------------------------------------------------------------------
</details>

<details>
<summary>HTTP Request Methods</summary>
<br>
  Is an operation you can run on a resourse on the web server.
  
  More info: https://www.owasp.org/index.php/Testing_for_HTTP_Verb_Tampering_(OTG-INPVAL-003) 
   
   Examining a web pages source code or a protocol analyzer you will be able to see when certain requests are used.
   
   For example seeing the code:
   
      <form action="webpage/" method=POST>
      <input type="Submit">
      
   As soon as you hit that "Submit" button it will send a POST request. 
   
   When you hit enter on the URL box in a browser it will send a GET.
   
   
    GET
        - Typically only for information retreval (no change in backend)
        - Pass parameters. They are passes in the URL
        - Change things in databases
       
    POST
        - Form submissions
        - The data is in the message body (unlike GET)
        
    OPTIONS
        - For a resource this will show all the supported request methods.
        - Not every web server has it enabled.
    
    HEAD
        - Response identical to GET minus the message body. 
        - Historically there have been Authentication bypass vulns with HEAD. Where auth was to POST and GET only.
    TRACE
        - Echos back the client req back for diagnostics
        
    PUT
        - Stores in URI
    
    DELETE
        - Delete resources
  
</details>


<details>
<summary>Authentication in HTTP</summary>
<br>
   Only two types of auth in the HTTP standard.
   
 ### Basic Authentication
      
       Note: This is all in place text.
       High view
       
   [![Capture.png](https://i.postimg.cc/fbXL63Z9/Capture.png)](https://postimg.cc/wtqgNj1q)  
               
----------------------------------------------------------------------------------------               
               
   [![Capture1.png](https://i.postimg.cc/Y0V05Q4Q/Capture1.png)](https://postimg.cc/YL6tgGzS)
        
        Notice the new http header in the 401 unauthorized that was the response to our request to the server.
        The initial request does not have this http header authentication portion.
         
        
        WWW.Authenticate: Basic  - the type of HTTP auth
        
        realm= "" - Set up by admin
        
         This tells the browser on the client what is being used and how to respond with creds.
         
  [![Captu2re.png](https://i.postimg.cc/wTw3Y8N9/Captu2re.png)](https://postimg.cc/2VBCntTt)        
         
         In the client response there is now an Authorization header with the credentials.
         The base64 encoded line beside Authorization is the username and pass combined together and encoded.
   
         The next server response is either a 401 unauthorized or 200 success.
          
    
    
   ### Digest Authentication
      
      Sends Hash of password (digest auth).
      
   <details>
   <summary>   RFC 2069 - General/original Digest Auth</summary>
   <br>
            Client - Server header communication for Digest Auth.
     
   [![Capture.png](https://i.postimg.cc/RZNK6wJt/Capture.png)](https://postimg.cc/G4nH68Q3)
      
       Calculating the "Response" portion of the header.
      
      Hash1 = MD5(Username:Realm:Password)
      Hash2 = MD5(Request method:URI)
      Response = MD5(Hash1:Nonce:Hash2)
      
      Note that opaque does nothing in RFC 2069 in creating the response.
      
   [![1.png](https://i.postimg.cc/yN5KPgP2/1.png)](https://postimg.cc/kVxLM5Ly)
   --------------------------------------------------------------------------------
   [![2.png](https://i.postimg.cc/xCHw3sqb/2.png)](https://postimg.cc/vgY2QtrQ)
   
   --------------------------------------------------------------------------------
       
       401 response with bad credentials
   
   [![3.png](https://i.postimg.cc/63sSqdz6/3.png)](https://postimg.cc/Ny4bP2WZ)
      --------------------------------------------------------------------------------
      
       200 OK response sent by the server if the credentials are good. 
   </details>
  
       
   
   ### HTTP Digest Authentication RFC 2617
   
    adds client nonce to help mitigate chosen plain text attacks
    
    adds Quality of Protection (QOP) 
      - auth for Authentication and auth-int for Authentication and Integrity (rarely used and not well supported)
      
     
      
   <details>
   <summary>More details for Digest Auth Hashing RFC 2069</summary>
   <br>
      Hash1 = MD5(Username:Realm:Password)
      Hash2 = MD5(Request method:URI)
      Response = MD5(Hash1:Nonce:Hash2)
   
   Creating HTTP Digest Auth hash response for RFC 2069 in Python
   
   import hashlib
   
   hash1 = hashlib.md5('USER:Realm:Password').hexdigest()
   
   hash2 = hashlib.md5('Request method:URI').hexdigest()
   
   nounce = XYZ
   
   response_string = hash1 + ':' + nonce + ':' + hash2
   
   response = hashlib.md5(response_string).hexdigest() 
   </details>
   
      
      
      
</details>










<details>
<summary></summary>
<br>
  
</details>
