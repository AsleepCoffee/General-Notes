# Same Origin Policy

SOP is a critical point of web app security. If a script on domain A was able to read content on domain B, it would be possible to steal client information and mount a number of dangerous attacks.

This policy prevents JS code from getting or setting properties on a resource coming from a differnt origin. 

To determine if JS can access a resource: Hostname, port and protocol must match.

    A JS script on 
    
       https://test.ca:345
      protocol  host   port
      
   Can read resources from: 
      
       https://test.ca:345/path
       https://test.ca:345/path/2 
       
   But not from:
      
        https://test.ca/path
        http://test.ca:345/path
        https://test2.ca:345/path
   
   
SOP applies only to the actual code of a script. It is still possible to include external resources by using HTML tages like img, script, iframe, object, etc.
