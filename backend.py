from flask import Flask, render_template, request, redirect, url_for
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import mysql.connector

app = Flask(__name__)

app.secret_key = 'dhaulagiri'

dbconfig = {    'host': '127.0.0.1',
                'user': 'mimi-db',
                'password': 'digital-nomad',
                'database': 'mountaineruDB',}

#Database connection details
#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'mimi-db'
#app.config['MYSQL_PASSWORD'] = 'digital-nomad'
#app.config['MYSQL_DB'] = 'mountaineruDB'

#Initialize MySQL
#mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('homepage'))

@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    return render_template('home.html', the_title="Search for your perfect Himalayan adventure!")

@app.route('/about', methods = ['POST', 'GET'])
def about():
    return render_template('about.html', the_title="About Mountaineru")

@app.route('/result', methods = ['POST', 'GET'])
def do_search() -> 'html':
    if request.method == 'POST':
        #searchquery = request.form['searchquery']
        #datefrom = request.form['datefrom']
        #dateto = request.form['dateto']
        #difficulty = request.form.getlist('difficulty') 
        
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """SELECT * FROM MountainTour"""
        cursor.execute(_SQL)
        searchresult = cursor.fetchall()

        cursor.close()
        conn.close()

        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute('''SELECT * FROM MountainTour''')
        # Fetch all record and return result
        #searchresult = cursor.fetchall()

    return render_template('result.html', output_data=searchresult)

if __name__ == '__main__':
    app.run(debug=True)
