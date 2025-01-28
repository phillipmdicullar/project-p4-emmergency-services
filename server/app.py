#!/usr/bin/env python3

# Remote library imports
from flask import Flask, make_response
from flask_migrate import Migrate
from config import app, db, api
from models import User, EmergencyPost, Response  
from flask_restful import Resource

migrate = Migrate(app, db)
class EmergencyPost(Resource):
    def get(self):
        response_to_dict = [n.to_dict for n in EmergencyPost.all()]
        make_response = {
            response_to_dict,
            200
        }
        # return {"emergency": "Someone is injured in 201"}
        return make_response
api.add_resource(EmergencyPost, '/emergency') 

if __name__ == "__main__":
    app.run(port=5555, debug=True)
