import sqlite3
z='information.db'
con= sqlite3.connect(z)
cur=con.cursor()

cur.execute("INSERT INTO info (username,password) VALUES ('eviro','1234567890e'), ('eyad','1234567890e')")

con.commit()
con.close()
