from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "ssssssssssssssssssshhh"

@app.route('/')
def index():
    mysql = connectToMySQL('friends')
    friends = mysql.query_db("SELECT * FROM friends")

    return render_template("index.html", friends = friends)

@app.route('/addfriend', methods = ['POST'])
def addFriend():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be left blank")
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be left blank")
    if len(request.form['occupation']) < 1:
        flash("Occupation cannot be left blank")
    
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        mysql = connectToMySQL('friends')
        # first_name = str(request.form['first_name'])
        # last_name = str(request.form['last_name'])
        # occupation = str(request.form['occupation'])
        # # newFriend = mysql.query_db("INSERT INTO friends (first_name, last_name, occupation, created_at, "+
        #     "updated_at) VALUES ('"+ first_name +"', '"+ last_name +"', '"+ occupation +"', NOW(), NOW());")
        query = ("INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) "+
            "VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());")
        data = {
            'first_name'    :   request.form['first_name'],
            'last_name'     :   request.form['last_name'],
            'occupation'    :   request.form['occupation']
        }
        newFriend = mysql.query_db(query, data)
        print(newFriend)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)