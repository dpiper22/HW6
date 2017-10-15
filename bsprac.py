import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

new_url = input('newfile.txt')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for x in tags:    
	print(x.get('href', None))