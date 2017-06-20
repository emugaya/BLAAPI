from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from bucketlists import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return (value.strftime("%Y-%m-%d") +" "+ value.strftime("%H:%M:%S"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column('password', db.String(20))
    date_created = db.Column(db.DateTime)
    date_modified =db.Column(db.DateTime)
    # bucketlists = db.relationship('BuckelList', backref='author', lazy='dynamic')

    def __init__(self , username ,password , email):
        self.username = username
        self.email = email
        self.password = password
        self.date_created = datetime.utcnow()
        self.date_modified = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


class BucketList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    # created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    items= db.relationship('Item', backref='bucket_list', lazy='dynamic')

    def __init__(self, name=None):
        self.name = name
        self.date_created = datetime.utcnow()
        self.date_modified = datetime.utcnow()
        # self.created_by = created_by

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'name' : self.name,
            'date_created' : dump_datetime(self.date_created),
            'date_modified' : dump_datetime(self.date_modified)
        }

    def serialize_id(self, item):
        """Return object data in easily serializeable format"""
        #self. item = b_items
        return {
            'id' : self.id,
            'name' : self.name,
            'items' : item,
            'date_created' : dump_datetime(self.date_created),
            'date_modified' : dump_datetime(self.date_modified)
        }

    # def __repr__(self):
    #      return '<Bucketlist %>' % self.name


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    date_created = db.Column(db.DateTime)
    date_modified = db.Column(db.DateTime)
    done = db.Column(db.Boolean)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucket_list.id'))

    def __init__(self, name, bucketlist_id):
        self.name = name
        self.date_created = datetime.utcnow()
        self.date_modified = datetime.utcnow()
        self.done = False
        self.bucketlist_id = bucketlist_id
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'name' : self.name,
            'date_created' : dump_datetime(self.date_created),
            'date_modified' : dump_datetime(self.date_modified),
            'done' : self.done,
        }

    def __repr__(self):
        return '<Item $>' % self.name
