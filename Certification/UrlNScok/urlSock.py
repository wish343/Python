__author__ = 'wIsh'

import urllib.request

local_filename, headers = urllib.request.urlretrieve('http://www.pythonlearn.com/code/intro-short.txt')
html = headers
print(html)
#connection.info().dict #For getting headers from urlopen
file = open(local_filename)
data = file.read()
#print(data)