""" Where we initialize our application and bring together different components """

from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#import mysql.connector
#import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YouWillNeverGuess'
#app.secret_key = 'dhaulagiri'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mimiDB:digital-nomad@localhost/mountaineruDB'
#db = SQLAlchemy(app)

from flask import render_template, request, redirect, url_for
from meru.forms import SearchForm

@app.route('/', methods = ['POST'])
@app.route('/home', methods = ['POST'])
def home():
    form = SearchForm()
    return render_template('index.html', form=form)


# @app.route('/compare', methods=['GET', 'POST'])
# def compare():
#     """ form = SearchForm()
#     if form.validate_on_submit():
#         flash(f'Search results for {form.adventure.data}!', 'success')
#         return redirect(url_for('homepage')) """
#     return render_template('compare.html')
#
#
# @app.route('/contact', methods = ['GET'])
# def contact():
#     return render_template('contact.html')
#
# @app.route('/result', methods = ['POST', 'GET'])
# def result() -> 'html':
#     """
#     if request.method == 'POST':
#         searchquery = request.form['searchquery']
#         month = request.form['month']
#         year = request.form['year']
#         difficulty = request.form['difficulty']
#
#
#         conn = mysql.connector.connect(host='127.0.0.1',
#                                     user=os.environ['DB_USER'],
#                                     password=os.environ['DB_PASSWORD'],
#                                     database='mountaineruDB')
#         cursor = conn.cursor()
#         _SQL = """ """ SELECT * FROM MountainTour
#                 WHERE TourName LIKE %s
#                 AND month(StartDate) = %s
#                 AND year(StartDate) = %s
#                 AND Difficulty = %s """ """
#         args = ('%' + searchquery + '%'), month, year, difficulty
#         cursor.execute(_SQL, args)
#         searchresult = cursor.fetchall()
#         cursor.close()
#         conn.close()
#      """
#     return render_template('category.html')