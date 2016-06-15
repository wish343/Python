__author__ = 'wIsh'

import urllib.request
import urllib.parse
import json

startURL = 'http://python-data.dr-chuck.net/geojson?'
address = input('Enter the University: ')

link = startURL + urllib.parse.urlencode({'sensor': 'false', 'address': address}) #Creating URL
print(link) #Printing the link
dataHandle = urllib.request.urlopen(link)
data = dataHandle.readall().decode('utf-8') #Converting data from bytes
#print(data)
#Converting the data to dictionary using json API
jsonD = json.loads(data)
#print(json.dumps(jsonD, indent = 4)) #Indenting and printing beautifully
results = jsonD['results'][0] #Getting first element in list inside the dictionary
print(results['place_id'])