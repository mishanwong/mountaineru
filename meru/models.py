""" This is for database classes """

from datetime import datetime
from meru import db

class Trip(db.Model):
    """ Data model for trekking trips """

    __tablename__ = 'mountaineru-trip'
    trip_id = db.Column(db.Integer, 
                        primary_key = True)
    trek_id = db.Column(db.Integer,     
                        index=False,
                        unique=False, 
                        nullable=False)
    trek_name = db.Column(db.String(80), 
                          index=False,
                          unique=False,
                          nullable=False)
    trek_code = db.Column(db.String(10),
                          index=False,
                          unique=False,
                          nullable=False)
    start_date = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=False)
    end_date = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    difficulty = db.Column(db.String(20),
                           index=False,
                           unique=False,
                           nullable=False)
    price = db.Column(db.Float,
                      index=False,
                      unique=False,
                      nullable=False)
    guide_company_id = db.Column(db.Integer,
                                 index=False,
                                 unique=False,
                                 nullable=False)
    guide_company = db.Column(db.String(128),
                              index=False,
                              unique=False,
                              nullable=False) 

#not sure what this is
def __repr__(self):
    return f"Trip('{self.trek_name}', '{self.trip_id}')"