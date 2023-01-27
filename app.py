from flask import Flask , request , render_template
from flask import url_for , flash , redirect , session
import sqlite3

app = Flask(__name__)
app.secret_key="123"
x= 'pharmacy.db'
db=sqlite3.connect("pharmacy.db")  

z='information.db'
con=sqlite3.connect(z)  

# firsr page to go to  signup page or login page

@app.route('/')
@app.route('/registration' , methods=['GET','POST']) 
def registration():
    return render_template('registration.html')

#signup page
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='GET':
     return render_template('signup.html')
    else:
        new=(
              request.form['name'],
              request.form['PhoneNumber'],
              request.form['username'],
              request.form['email'],
              request.form['password']
        )
        insert(new)
        return redirect (url_for ('login'))
        
#function that post the information from signup page to information database
def insert(new):
    con=sqlite3.connect(z)    
    cur=con.cursor()
    sql_execute_strin = 'INSERT INTO info (name,PhoneNumber,username,email,password) VALUES (?,?,?,?,?)'
    cur.execute(sql_execute_strin, new)
    con.commit()
    con.close()

#login page
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        con=sqlite3.connect(z)
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from info where username=? and password=?",(username,password))
        data=cur.fetchone()

        if data:
            session["name"]=data["name"]
            session["email"]=data["email"]
            session["id"]=data["id"]


            return redirect("home")
        else:
            flash("Username and Password invalid","danger")

    return render_template('login.html')
        

#logout page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("registration"))



#profile page
@app.route('/profile', methods=['GET','POST'])  
def profile():
    con=sqlite3.connect(z)
    cur=con.cursor()
    cur.execute(f"select * FROM info where id={session['id']};")
    row=cur.fetchone() 
    con.close() 
    return render_template('profile.html' , row = row)   



#home page
@app.route('/home', methods=['GET','POST'])
def home():
    data_table= display()
    return render_template('home.html',data_table=data_table)

# funtion to get data from pharmacy database
def display():
    db=sqlite3.connect(x)    
    c=db.cursor()
    c.execute(""" SELECT * FROM medicine """) 
    data= c.fetchall()
    return data



# Add medicine page
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method=='GET':
     return render_template('add.html')
    else:
        newdata=(
            request.form['medicine'],
            request.form['code'],
            request.form['price'],
            request.form['expiry_date'],
            request.form['therapeutic_indications'],
            request.form['side_effects'],
            request.form['storage']
        )
        insert_data(newdata)
        return redirect (url_for ('home'))
        

# function to insert new data in pharmacy database 
def insert_data(newdata):
    db=sqlite3.connect(x)    
    c=db.cursor()
    sql_execute_string = 'INSERT INTO medicine (medicine,code,price,expiry_date,therapeutic_indications,side_effects,storage) VALUES (?,?,?,?,?,?,?)'
    c.execute(sql_execute_string, newdata)
    db.commit()
    db.close()


# update page that update the data in information database
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    # print(request.method)
    if request.method=='POST':

        medicine= request.form['medicine']
        code= request.form['code']
        price=request.form['price']
        expiry_date=request.form['expiry_date']
        therapeutic_indications= request.form['therapeutic_indications']
        side_effects=request.form['side_effects']
        storage= request.form['storage']
        print("hello")
        print(medicine,price,code,expiry_date,therapeutic_indications,storage)
        # print(request.form)
        db=sqlite3.connect(x)    
        db.execute(f"update medicine set medicine= '{medicine}',code='{code}',price='{price}',expiry_date='{expiry_date}',therapeutic_indications='{therapeutic_indications}',side_effects='{side_effects}',storage='{storage}' where id ={id};")
        db.commit()
        db.close()
        return redirect (url_for ('home'))

    db=sqlite3.connect(x)
    c=db.cursor()
    c.execute(f"select * from medicine where id = {id};")
    row=c.fetchone() 
#    print(row)
    db.close() 
    return render_template('update.html' , row = row)   



# Delete data from information database
@app.get('/delete/<int:id>')
def delete(id):
    db=sqlite3.connect(x)    
    c=db.cursor()
    c.execute(f""" delete  FROM medicine where id ={id};""") 
    db.commit()
    db.close()
    return redirect (url_for ('home'))

#Search on data by name in the information database
@app.post('/search')
def search():
    name=request.form['search']
    db=sqlite3.connect(x)    
    c=db.cursor()
    c.execute(f""" select * FROM medicine where medicine like '%{name}%';""")
    data=c.fetchall()
    return render_template ('home.html',data_table=data)


# Delete the profile from information database
@app.get('/delprof')
def delprof():
    con=sqlite3.connect(z)    
    cur=con.cursor()
    cur.execute(f""" delete FROM info where id={session['id']};""") 
    con.commit()
    con.close()
    return redirect (url_for ('registration'))    



if __name__ == '__main__':
    app.run(debug=True)


## run the confirm password
## add photo to signup page and display it in profile data base
##update the data in profile page (information database)
## click on medicine name to move to another page( describe page) that display all details of medicine
## add photo of medicine in add page and display it in the decribe page
# adding function to search on price and therapeutic indications


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

# if __name__ == "__main__":
#     app.run()    