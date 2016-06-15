__author__ = 'wIsh'

import urllib.request
import xml.etree.ElementTree as ET

link = input('Enter the URL: ')
if len(link) < 1:
	link = 'http://python-data.dr-chuck.net/comments_282560.xml'
link1 = 'http://python-data.dr-chuck.net/comments_42.xml'

#link = link1              #uncomment to run sample xml

file = urllib.request.urlopen(link)
data = file.read()
eTree = ET.fromstring(data)
countsList = eTree.findall('comments/comment')
counts = sum([int(x.find('count').text) for x in countsList]) #x.get(attribute)
print(counts)
