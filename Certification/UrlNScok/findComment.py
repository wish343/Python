__author__ = 'wIsh'

import urllib.request
from bs4 import BeautifulSoup as bs


countt = 0
summ = 0
urlK = input('Enter - ')
if len(urlK) < 1:
	urlK = 'http://python-data.dr-chuck.net/comments_282563.html'
file1 = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.html')
file2 = urllib.request.urlopen(urlK)
soup = bs(file2, "html.parser") #Change to file1 for sample file
tags = soup('span')
for item in tags:
	summ += int(item.contents[0])
	countt += 1
	#item.get('href',None) #None is default
	#item.attrs
print('Count',countt)
print('Sum',summ)