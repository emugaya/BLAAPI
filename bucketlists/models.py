from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     # password =
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# class BuckelLists(db:Model):
#     id = db.column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     date_created = db.Column(db.DateTime)
#     date_modified = db.Column(db.DateTime)
#     creted_by =
