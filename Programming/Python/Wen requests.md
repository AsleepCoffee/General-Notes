# Web requests

import requests


Making the requests: 

 URL=""
 
 r=requests.session()
 out=r.get(url)
 
 
 ## Searching responses
 
 import re
 
 out=re.search("<regex>",out.text)
