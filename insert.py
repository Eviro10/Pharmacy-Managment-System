import sqlite3
x='pharmacy.db'
db= sqlite3.connect(x)
c=db.cursor()

c.execute(""" 
 INSERT INTO medicine (Medicine,Code,price,expiry_date,therapeutic_indications,side_effects,storage) VALUES
('Congestal','uf25','50','1 year','cold','insomnia',' in a dry place at temperature not exceeding 25 C'),
('brofen','cf22','59.5','3 years','fever','insomnia',' in a dry place at temperature not exceeding 25 C')
""")

db.commit()
db.close()
