#  Database models for the required db schema
from datetime import datetime
from app import db



class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    distance = db.Column(db.Integer, nullable = False)
    rate = db.Column(db.Integer, nullable = False)
    project_size = db.Column(db.Integer, nullable = False)
    completion_date = db.Column(db.Date, nullable = False)


class Order(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	col_name = db.Column(db.String(128), nullable= False, unique= True)
	priority_2 = db.Column(db.String(128), nullable = False)
	priority_3 = db.Column(db.String(128), nullable = False)
	priority_4 = db.Column(db.String(128), nullable = False)


