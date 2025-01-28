#!/usr/bin/env python3

# Remote library imports
from flask import Flask, make_response, request
from flask_migrate import Migrate
from config import app, db, api
from models import User, EmergencyPost, Response  
from flask_restful import Resource

migrate = Migrate(app, db)
class Home(Resource):
    def get(self):
        return make_response({"message": "Welcome to Emergency Response API"}, 200)
api.add_resource(Home, '/')

class EmergencyPostResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in EmergencyPost.query.all()]
        return make_response(response_dict_list, 200)

    def post(self):

        incoming_data = request.get_json()
    
        data = EmergencyPost(
            location=incoming_data.get("location"),
            type=incoming_data.get("type"),
            description=incoming_data.get("description"),
            user_id=incoming_data.get("user_id")
        )
        db.session.add(data)
        db.session.commit()
        

        response = {
            "message": "post created successfully",
            "data": data.to_dict()
        }
        
        return make_response(response, 201)
api.add_resource(EmergencyPostResource, '/emergencies') 



if __name__ == "__main__":
    app.run(port=5555, debug=True)
