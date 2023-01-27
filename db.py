import sqlite3

db=sqlite3.connect("pharmacy.db")    
c=db.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS medicine
(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   medicine TEXT,
   code Text,
   price FLOAT,
   expiry_date TEXT,
   therapeutic_indications TEXT,
   side_effects TEXT,
   storage TEXT
)
""")

db.commit()
db.close()