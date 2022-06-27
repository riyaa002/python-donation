from flask import Flask,render_template,url_for, request, redirect,flash
import os
import sqlite3
import razorpay
currentlocation = os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__,template_folder='template')



#--------ROUTE LOGIN PAGE-----------

@app.route('/')
def home1():
    return render_template('home1.html')
 
@app.route('/login')
def login():
    return render_template('login.html')

#--------login database--------
@app.route('/login',methods=['POST','GET'])
def ulogin():
    error = "Invalid Username or password"
    if request.method=='POST':
        lemail = request.form['lemail']
        lpassword = request.form['lpassword']
        con = sqlite3.connect("Users.db")
        cursor = con.cursor()
        query1 = "SELECT email,password FROM Users WHERE email='"+lemail+"' AND password='"+lpassword+"'"
        row = cursor.execute(query1)
        rows = row.fetchone()
        if rows:
            return render_template('/home.html',name=lemail)
        else:
            return render_template('/login.html',error=error)


#--------ROUTE SIGNIN PAGE-----------
@app.route('/signin')
def signin():
    return render_template('signin.html')

#----------signin database----------
@app.route('/signin',methods=['POST','GET'])
def usignin(): 
    if request.method=='POST':
        error = "Password does not match!"
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        confirmp=request.form['confirmp']
        

        sqlconnection = sqlite3.Connection(currentlocation + r'\Users.db')
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{n}','{e}','{p}','{cp}')".format(n=name,e=email,p=password,cp=confirmp)
        cursor.execute(query1)
        sqlconnection.commit()

        if confirmp == password:
            return render_template('/login.html')
        else:    
            return render_template('/signin.html',error = error)



#--------ROUTE home PAGE-----------

@app.route('/home')
def home():
    return render_template('home.html')




#--------ROUTE DONATE PAGE-----------
@app.route('/donate')
def donate():
    return render_template('donate.html')


#--------ROUTE COVID PAGE-----------
@app.route('/covid')
def covid():
    return render_template('covid.html')



#--------ROUTE Oldage PAGE-----------
@app.route('/oldage')
def oldage():
    return render_template('oldage.html')

#--------ROUTE orphanage PAGE-----------
@app.route('/orphanage')
def orphanage():
    return render_template('orphanage.html')


#--------ROUTE cancer PAGE-----------
@app.route('/cancer')
def cancer():
    return render_template('cancer.html')


#--------ROUTE about us PAGE-----------
@app.route('/about us')
def aboutus():
    return render_template('about us.html')

#--------ROUTE FUNDRAISER PAGE-----------
@app.route('/fundraiser')
def fundraiser():
    return render_template('fundraiser.html')


#--------ROUTE Fundraiser categories PAGE-----------
@app.route('/fundcat')
def fundcat():
    return render_template('fundcat.html')

@app.route('/fsuccess')
def fsuccess():
    return render_template('fsuccess.html')



#--------ROUTE VOLUNTEER PAGE-----------
@app.route('/volunteer')
def volunteer():
  
    return render_template('volunteer.html')

@app.route('/vsuccess')
def vsuccess():
    return render_template('vsuccess.html')

if __name__  == "__main__":
    app.run(debug=True)
