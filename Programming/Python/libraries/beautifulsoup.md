ref: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup as bs4


## parsing data

parser = bs4(<page response>, '<parser>'
  
  
## finding data after parsing

out = parser.find('string', 'tag', 'etc')

out = parser.find_all('string', 'tag', 'etc')



## output 

<parsed output>.text   # removes any code (HTML, or w.e was parsed) adn just leaves text values
