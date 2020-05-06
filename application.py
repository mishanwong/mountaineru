from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

application = app = Flask(__name__)

app.secret_key = 'dhaulagiri'

dbconfig = {    'host': 'aa1c3p2qmazyyc1.cpksfpeuyyky.us-west-2.rds.amazonaws.com',
                'user': 'mimineruDB',
                'password': 'digital-nomad',
                'database': 'MountaineruDB',
                'port': 3306,}

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
        searchquery = request.form['searchquery']
        month = request.form['month']
        year = request.form['year']
        difficulty = request.form['difficulty']
        
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """SELECT * FROM MountainTour
            WHERE TourName LIKE %s
            AND month(StartDate) = %s
            AND year(StartDate) = %s
            AND Difficulty = %s """
        args = ('%' + searchquery + '%'), month, year, difficulty
        cursor.execute(_SQL, args)
        searchresult = cursor.fetchall()

        cursor.close()
        conn.close()

    return render_template('result.html', output_data=searchresult)

if __name__ == '__main__':
    application.run(debug=True)
