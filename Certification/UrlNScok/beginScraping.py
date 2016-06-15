__author__ = 'wIsh'

from bs4 import BeautifulSoup as bs
import urllib.request

counter = 0
link = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

if len(link) < 1:
	link = 'http://python-data.dr-chuck.net/known_by_Will.html'
link1 = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

#link = link1 #uncomment for sample link run

while counter < count:
	print('Retrieving:',link)
	file = urllib.request.urlopen(link)
	soup = bs(file, 'html.parser')
	tags = soup('a')
	theTag = tags[position]
	link = theTag.get('href', None)
	counter += 1

	#name = theTag.contents[0]
print('Retrieving:',link)
name = theTag.contents[0]
print(name)
