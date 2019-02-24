#This uses urlopen to access a site, then uses BeautifulSoup to get the
#HTML from that site, and then cuts out all of the non-text
from urllib.request import urlopen
from bs4 import BeautifulSoup
site = urlopen("https://www.utdallas.edu")
soup = BeautifulSoup(site, "html.parser")
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
print(visible_text)