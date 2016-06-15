__author__ = 'wIsh'

import urllib.request
import json

link = input('Enter URL: ')
if len(link) < 1:
	link = 'http://python-data.dr-chuck.net/comments_282564.json'
link1 = 'http://python-data.dr-chuck.net/comments_42.json'

#link = link1 #Un-comment to read sample JSON

dataHandle = urllib.request.urlopen(link) #Opening the link
data = dataHandle.readall().decode('utf-8') #Converting to utf-8 format
#print(data)

jsonForm = json.loads(data) #Creating dictionary
comments = jsonForm['comments'] #Getting list

sumS = 0
for item in comments:
	sumS += item['count']
print(sumS)