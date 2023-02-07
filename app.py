from flask import Flask,request,jsonify,make_response
from flask_cors import CORS
#ช่วยชีวิตต่อการเติม host = host , db = db
from flask_mysqldb import MySQL
import json
import mysql.connector
import MySQLdb.cursors



app = Flask(__name__)

#intialize mysql 
mysql_combo = MySQL(app)

#all configure
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '02749'
app.config['MYSQL_DB'] = 'api_test'
app.config['JSON_AS_ASCII'] = False


#Testing api 
@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"


# #Practice GET Function
# @app.route('/api/attraction')
# def  read():
#     mydb = mysql.connector.connect(host = host , user = user , password = password , db =db)
#     mycursor = mydb.cursor(dictionary = True)
#     mycursor.execute("SELECT * FROM attraction  ")
#     myresult = mycursor.fetchall()
#     return make_response(jsonify(myresult),200)


# anirach style
#fetchon is tuple and fetcahll josntify 
@app.route('/api/attraction')
def  read():
   cursor = mysql_combo.connection.cursor()
   cursor.execute("SELECT * FROM attraction  ")
   acept = cursor.fetchall()
   print(acept)
   print(type(acept))
   return make_response(jsonify(acept),200)





#Practice GET Function by id
@app.route('/api/attraction/<int:id>')
def  readbyid(id):
    cursor = mysql_combo.connection.cursor()
    query = "SELECT * FROM api_test.attraction WHERE id = %s  "
    parameters = (id,)
    print("Query: ", query)
    print("Parameters: ", parameters)
    cursor.execute(query, parameters)
    acept = cursor.fetchall()
    return make_response(jsonify(acept),200)
     

#POST function  by create  data into table
@app.route('/api/create', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    detail = data['detail']
    cursor = mysql_combo.connection.cursor()
    cursor.execute("INSERT INTO attraction (name, detail) VALUES (%s, %s)", (name, detail))
    mysql_combo.connection.commit()
   
    return {"sucess":"Yeah"}
   

#Update api PUT
@app.route('/api/attraction/<int:id>' , methods = ['PUT'])
def update(id):
    data = request.get_json()
    name = data['name']
    detail = data['detail']
    cursor = mysql_combo.connection.cursor()
    cursor.execute("UPDATE attraction SET name = %s, detail = %s WHERE id = %s", (name, detail, id))
    mysql_combo.connection.commit()
    return make_response(jsonify({"rowcount": cursor.rowcount}))



#Del  api DEL
@app.route("/api/attraction/<int:id>" , methods =['DELETE'])
def delete(id):
    cursor = mysql_combo.connection.cursor()
    query = "DELETE FROM attraction WHERE id = %s ;"
    parameter = (id , )
    cursor.execute(query,parameter)
    mysql_combo.connection.commit()
    
    return make_response(jsonify({"DELETE row ": cursor.rowcount}))

if __name__ == '__main__':
    app.run(debug= True)