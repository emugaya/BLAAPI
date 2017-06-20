
from flask import Flask, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from bucketlists import app, db
from bucketlists.models import BucketList, User, Item
from sqlalchemy.orm import class_mapper, session, sessionmaker
from json import dumps
from datetime import datetime, date

api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Helloworld, '/v1/')

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('buckect_list_id')

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return (value.strftime("%Y-%m-%d") +" "+ value.strftime("%H:%M:%S"))

#Get list of all BucketLists and add BucketList
class BucketListView(Resource):
    def get(self):
        bucket_lists = BucketList.query.all()
        return make_response(jsonify([i.serialize for i in bucket_lists]))

    def post (self):
        args = parser.parse_args()
        new_bucketlist = BucketList(args.name)
        db.session.add(new_bucketlist)
        db.session.commit()
        return 201

# Add resource for Adding single bucket list and listing all created bucket lists
api.add_resource(BucketListView,'/v1/bucketlists/')

#Display/View/Get, Delete, Update Single BucketList
class BucketListViews(Resource):
    def get(self, buckect_list_id):
        args = parser.parse_args()
        bucket_list_item = BucketList.query.filter(BucketList.id == buckect_list_id).all()
        single_bucket_list_items = Item.query.filter(Item.bucketlist_id == buckect_list_id).all()
        b_item = ([i.serialize for i in single_bucket_list_items])
        x  = 1
        return  make_response(jsonify([i.serialize_id(b_item) for i in bucket_list_item]))
        # return  ([i.serialize for i in single_bucket_list_items])

    def delete(self, buckect_list_id):
        pass

    def put(self, buckect_list_id):
        pass

# Add resource for getting, updating, and deleting a single bucket list
api.add_resource(BucketListViews,'/v1/bucketlists/<buckect_list_id>')

#Create a new item in BucketLists
class BucketListItem(Resource):
    def post(self):
        pass

#Add Resources for creating or adding newbucket list item
api.add_resource(BucketListItem,'/v1/bucketlists/<id>/items/')

# Update and Delete Bucket List item
class BucketListItems(Resource):
    def put(self):
        pass

    def post(self):
        pass
# Add Resource for updating and deleting bucket list items
api.add_resource(BucketListItems,'/v1/bucketlists/<id>/items/<item_id>')
