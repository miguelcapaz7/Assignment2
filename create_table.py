import sqlite3

conn = sqlite3.connect('songs.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE Song
          (id INTEGER PRIMARY KEY ASC, 
           title TEXT NOT NULL,
           artist TEXT NOT NULL,
           runtime TEXT NOT NULL,
           pathname TEXT NOT NULL,
           filename TEXT NOT NULL,
           album TEXT,
           genre TEXT,
           date_added TEXT NOT NULL,
           last_played TEXT,
           play_count INTEGER NOT NULL,
           rating INTEGER)
          ''')

conn.commit()
conn.close()