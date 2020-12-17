# Web requests

import requests

https://realpython.com/python-requests/

Making the requests: 

 URL=""
 
Proxies

  proxies = {"http": "http://<proxy IP>:8080", "https": "http://<proxy IP>:8080"}
 
Cookies

  cookies = {'<cookie name>': '<value>'}
 
 Requests: 
  
  Add verify=False if you want to ignore ssl errors
  
   r = requests.get( url )
  
    
 
 ## Searching responses
 
 import re
 
 out=re.search("<regex>",out.text)
