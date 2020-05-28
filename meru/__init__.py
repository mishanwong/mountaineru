""" Where we initialize our application and bring together different components """ 

from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#import mysql.connector
#import os

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'YouWillNeverGuess'
#app.secret_key = 'dhaulagiri'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mimiDB:digital-nomad@localhost/mountaineruDB'
#db = SQLAlchemy(app)

from meru import routes