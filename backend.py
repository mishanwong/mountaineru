from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

app.secret_key = 'dhaulagiri'

dbconfig = {    'host': '127.0.0.1',
                'user': 'mimi-db',
                'password': 'digital-nomad',
                'database': 'mountaineruDB' }

@app.route('/')
def index():
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = '''select * from MountainTour''' #Insert SQL query here
    cursor.execute(_SQL)
    results = cursor.fetchall()
    return results #redirect(url_for('homepage'))

@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    return render_template('home.html', the_title="Search for your perfect Himalayan adventure!")

@app.route('/about', methods = ['POST', 'GET'])
def about():
    return render_template('about.html', the_title="About Mountaineru")

"""
@app.route('/result', methods = ['POST', 'GET'])
def do_search() -> 'html':
    searchquery = request.form['searchquery']
    datefrom = request.form['datefrom']
    dateto = request.form['dateto']
    difficulty = request.form.getlist('difficulty')
    title = 'Here are what you searched for: '
    return render_template('result.html', the_title=title, the_searchquery=searchquery, the_datefrom=datefrom, the_dateto=dateto, the_difficulty=list(difficulty),)
"""

if __name__ == '__main__':
    app.run(debug=True)
