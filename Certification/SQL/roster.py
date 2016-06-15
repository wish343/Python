__author__ = 'wIsh'

import sqlite3
import json

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

#Table creation
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
	id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name   TEXT UNIQUE
);

CREATE TABLE Course (
	id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title  TEXT UNIQUE
);

CREATE TABLE Member (
	user_id     INTEGER,
	course_id   INTEGER,
	role        INTEGER,
	PRIMARY KEY (user_id, course_id)
)
''')

#Getting data from file
fileName = input('Please enter the File Name: ')
if len(fileName) < 1:
	fileName = 'roster_data.json'


dataRaw = open(fileName).read()
data = json.loads(dataRaw)
#Data looks like this
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#Adding data to tables
for item in data:
	name = item[0]
	title = item[1]
	role = item[2]

	#User
	cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name, ))
	cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
	userId = cur.fetchone()[0]

	#Course
	cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title, ))
	cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
	courseId = cur.fetchone()[0]

	#Member
	cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''', (userId, courseId, role))

conn.commit()
cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
	User JOIN Member JOIN Course
	ON User.id = Member.user_id AND Member.course_id = Course.id
	ORDER BY X
	''')
print(cur.fetchone()[0])
