from flask import Flask, render_template, request,url_for,session,redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os



app = Flask(__name__)

app.secret_key = 'Thismydatabase'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '02749'
app.config['MYSQL_DB'] = 'fitness'

#Intialize mysql
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():

     #the output for show message 
    msg = ''
    #Authenticating Users 
    #the method for check username 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        #create variable for access
        username = request.form['username']
        password = request.form['password']

        #check account exits using Mysql
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))

        # Fetch one record and return result
        account = cursor.fetchone()
    #If account exits in accoutn  table in database 
        if account : 
            #Create data session   
            session['loggedin'] = True
            session['id'] = account['id']
            session[username]= account['username']
            # Redirect to homepage 
            return 'Logged in successfully'

        else:
            #Account doesn't exit from DB
            msg = 'Incorrect username/password!'

    return render_template('index.html',msg=msg)


@app.route('/logout')
def logout():

    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    # Getout to login page

    return redirect(url_for('login'))




@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        usernames = request.form['username']
        password = request.form['password']
        email = request.form['email']
    
    elif request.method == 'POST':
    
        msg = 'Please fill out the form!'
    
    #check if account exits using Mysql

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = %s', (usernames,))
    # account = cursor.fetchone()

    # if account :
    #     msg = "Account already exists!!"
    
    # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    #     msg = "Invalid email address!!"
    
    # elif not re.match(r'[A-Za-z0-9]+',usernames):
    #     msg ='Username must contain only characters and numbers!'

    # elif not usernames or not password or not email:
    #     msg = 'Please fill the from '


    # else: 
    #     cursor('INSEART INTO accounts VALUES (NULL %s, %s, %s )',(usernames,password,email))
    #     mysql.connect.commit()
    #     msg = "You have  successfully registered !!"


    # return render_template('register.html', msg=msg)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

