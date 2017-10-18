from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



url = input('Enter -')
count = int(input("Enter Count: "))
position = int(input('Enter Position: '))


the_people = []
names = range(count)

for x in names:
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	url = soup.find_all('a')[position - 1].get('href')
	the_people.append(url)
print(the_people[-1])





