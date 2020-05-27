from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SearchForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'YouWillNeverGuess'
#app.secret_key = 'dhaulagiri'

@app.route('/')
@app.route('/home', methods = ['POST', 'GET'])
def homepage():
    return render_template('home.html', the_title="Home")

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash(f'Search results for {form.adventure.data}!', 'success')
        return redirect(url_for('homepage'))
    return render_template('search.html', the_title="Search your adventure", form=form)

@app.route('/about', methods = ['POST', 'GET'])
def about():
    return render_template('about.html', the_title="About")

@app.route('/result', methods = ['POST', 'GET'])
def do_search() -> 'html':
    if request.method == 'POST':
        searchquery = request.form['searchquery']
        month = request.form['month']
        year = request.form['year']
        difficulty = request.form['difficulty']
        
        
        conn = mysql.connector.connect(host='127.0.0.1', 
                                    user=os.environ['DB_USER'],
                                    password=os.environ['DB_PASSWORD'],
                                    database='mountaineruDB')
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
        
    return render_template('result.html', output_data=searchresult, the_title="Search results")

if __name__ == '__main__':
    application.run(debug=True)
