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

200 - OK

300 - Redirect

400 - Bad request

500 - Issue on the server side

### Request methods

GET

POST

## Host header

Tells the server what hostname we are interested in in relation to the page we are requesting.
This is for servers hosting multiple domains.

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
<summary></summary>
<br>
  
</details>
