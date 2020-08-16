# Same Origin Policy

Note: CSS stylesheets, images, and scripts are loaded by the browser without consulting the policy. 

SOP is a critical point of web app security. If a script on domain A was able to read content on domain B, it would be possible to steal client information and mount a number of dangerous attacks.

This policy prevents JS code from getting or setting properties on a resource coming from a differnt origin. 

Is defined by Protocol/Host/Port.

Note IE works slightly different: Does not consider the port as a componenet to the SOP and the SOP os not applied to  domains that are in highly trusted zone (i.e. corporate domains).

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

## Exceptions 

window.location: A document can always write the location property of another document if they have some relationship. But cannot read, except if the two docuemnts have the same origin. Means the location property can always be changed, but its the SOP that determines whether a new document can be loaded.

  Types of relationships: 
   
 - A doc is embedded with another via an iframe element
 - 1 doc is opened by the other via the window.open DOM API

document.domain: Describes the domain portion of the origin of the current doc. A doc can update its own document.domain to a higher level in the domain hie except for the TLD. The second-level domain (domain.com) can be specified but it cannot be changed. By changing document.domain a doc slightly changes its own origin. SOP can be circumvented if both sites have each others domain specified as document.domain=<domain>, this way the 2 docs are cosnidered in the same origin.

Cross window messaging: New HTML5 feature. premits diff docs (iframes, popups , and current window) to comm with each other regardless of the SOP by using simple synchronous mechanism.

CORS: Set of SPECS build to allow a browser to access a few resources by bypasssing the SOP. The CORS arch uses custom HTTP response headers and relies upon server-side components or server side languages. 
