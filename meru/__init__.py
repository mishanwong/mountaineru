""" Where we initialize our application and bring together different components """ 

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from config import Config
#import mysql.connector
#import os

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'YouWillNeverGuess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mountaineru.db'
db = SQLAlchemy(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mimiDB:digital-nomad@localhost/mountaineruDB'

from meru import routes