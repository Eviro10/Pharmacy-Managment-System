import sqlite3

db=sqlite3.connect("pharmacy.db")    
c=db.cursor()
c.execute(" SELECT * FROM medicine ")

info= c.fetchall()
for pharma in info:
    print(pharma)



db.commit()
db.close()