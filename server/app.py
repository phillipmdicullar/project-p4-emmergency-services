#!/usr/bin/env python3

# Remote library imports
from flask import Flask, make_response
from flask_migrate import Migrate
from config import app, db, api
from models import User, EmergencyPost, Response  
from flask_restful import Resource

migrate = Migrate(app, db)
class EmergencyPostResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in EmergencyPost.query.all()]
        return make_response(response_dict_list, 200)
api.add_resource(EmergencyPostResource, '/emergency') 

if __name__ == "__main__":
    app.run(port=5555, debug=True)
