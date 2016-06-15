__author__ = 'wIsh'
import sqlite3

#Use sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#Create table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT,count INTEGER)')

#Get file
fname = input("Please enter the file name: ")
if len(fname) < 1:
	fname = 'mob.txt'
handle = open(fname)

#Process Data
for line in handle:
	if not line.startswith('From: '):
		continue
	#Finding senders email
	data = line.split()
	email = data[1]
	#Finding Organization
	emailSplit = email.split('@')
	org = emailSplit[1]
	#Finding corresponding entry in table
	cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
	try:
		theCount = cur.fetchone()[0]
		cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (org, ))
	except:
		cur.execute('INSERT into Counts(org,count) VALUES (?,1)', (org, ))

conn.commit()
#For checking the data created
cur.execute('SELECT * FROM Counts ORDER BY count DESC')
while(True):
	data = cur.fetchone()
	if data is None:
		break
	print(data)