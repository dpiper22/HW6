from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/comments_39686.html"
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

numb = []
tags = soup('span')
for x in tags:
	numb.append(int(x.contents[0]))

sum_nums = sum(numb)

print(sum_nums)
