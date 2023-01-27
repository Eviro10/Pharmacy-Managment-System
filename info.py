import sqlite3

con=sqlite3.connect("information.db")    
cur=con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS info
(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   PhoneNumber INTEGER,
   username TEXT,
   email TEXT,
   password TEXT
)
""")

con.commit()
con.close()