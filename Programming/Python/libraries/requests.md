ref: https://requests.readthedocs.io/en/master/

import requests

**get request**

r = requests.get(url)

**output**

response = r.content

r.status_code


**basic auth**

r = requests.get(url, auth=(username, password))











