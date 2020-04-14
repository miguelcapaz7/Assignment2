import sqlite3

conn = sqlite3.connect('songs.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE Song
          ''')

conn.commit()
conn.close()
