
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from bucketlists import app
import bucketlists.models

api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Helloworld, '/v1/')

#Get list of all BucketLists and add BucketList
class BucketLists(Resource):
    def get(self):
        pass

    def post (self):
        pass

# Add resource for Adding single bucket list and listing all created bucket lists
api.add_resource(BucketLists,'/v1/bucketlists/')

#Display/View/Get, Delete, Update Single BucketList
class BucketList(Resource):
    def get(self, buckect_list_id):
        pass

    def delete(self, buckect_list_id):
        pass

    def put(self, buckect_list_id):
        pass

# Add resource for getting, updating, and deleting a single bucket list
api.add_resource(BucketList,'/v1/bucketlists/<id>')

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
