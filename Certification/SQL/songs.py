__author__ = 'wIsh'

import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;''')

#Create Tables required in the database
cur.execute('CREATE TABLE IF NOT EXISTS Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute(''' CREATE TABLE IF NOT EXISTS Genre (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name    TEXT UNIQUE
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Album (
	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id  INTEGER,
	title   TEXT UNIQUE
) ''')
cur.execute('''CREATE TABLE IF NOT EXISTS Track (
	id  INTEGER NOT NULL PRIMARY KEY
		AUTOINCREMENT UNIQUE,
	title TEXT  UNIQUE,
	album_id  INTEGER,
	genre_id  INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
)''')

#Getting File and opening
fileName = input('Please enter the File Name: ')
if len(fileName) < 1:
	fileName = 'Library.xml'

#ET can read data directtly from file and we don't have to use fromstring function
xmlData = ET.parse(fileName)
songList = xmlData.findall('dict/dict/dict')

#Function to find a particular tag in an entry
def lookup(entry, item):
	found = False
	for child in entry:
		if found:
			return child.text
		if child.tag == 'key' and child.text == item:
			found = True
	return None

#Traversing through the data
for item in songList:
	if lookup(item, 'Track ID') is None:
		continue

	name = lookup(item, "Name")
	artist = lookup(item, 'Artist')
	album = lookup(item, 'Album')
	count = lookup(item, 'Play Count')
	rating = lookup(item, 'Rating')
	length = lookup(item, 'Total Time')
	genre = lookup(item, 'Genre')

	#Checking if something was None
	if name is None or artist is None or album is None or genre is None:
		continue

	#Enter the data into Tables created
	#Artist
	cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
	cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
	artistId = cur.fetchone()[0]

	#Genre
	cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES(?)', (genre, ))
	cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
	genreId = cur.fetchone()[0]

	#Album
	cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES(?,?)', (artistId, album))
	cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
	albumId = cur.fetchone()[0]

	#Track
	cur.execute('''INSERT OR IGNORE into Track (title, album_id, genre_id, len, rating, count)
				VALUES (?, ?, ?, ?, ?, ?)''', (name, albumId, genreId, length, rating, count))

conn.commit()


#print(cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
#	FROM Track JOIN Genre JOIN Album JOIN Artist
#	ON Track.genre_id = Genre.ID and Track.album_id = Album.id
#		AND Album.artist_id = Artist.id
#	ORDER BY Artist.name LIMIT 3''').fetchone())