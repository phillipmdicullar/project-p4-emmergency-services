#!/usr/bin/env python3

# Remote library imports
from flask import Flask, make_response, request
from flask_migrate import Migrate
from config import app, db, api
from models import User, EmergencyResponse, EmergencyPost, Response  
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

class EmergencyResponseResource(Resource):

    def get(self, id):
        post = EmergencyPost.query.get_or_404(id)
        response_dict_list = [n.to_dict() for n in post.responses]
        return make_response(response_dict_list, 200)

    def put(self, id):
        incoming_data = request.get_json()
        data = EmergencyResponse(
            location=incoming_data.get("location"),
            type=incoming_data.get("type"),
            description=incoming_data.get("description"),
        )
        db.session.add(data)
        db.session.commit()
        response = {
            "message": "response created successfully",
            "data": data.to_dict()
        }
        return make_response(response, 201)

    def delete(self, id):
        post = EmergencyResponse.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return make_response({"message": "response deleted successfully"}, 200)
        
api.add_resource(EmergencyResponseResource, '/emergencies/<int:id>/responses')

class UserResource(Resource):
    def get(self):
        response_dict_list = [n.to_dict() for n in User.query.all()]
        return make_response(response_dict_list, 200)

    def post(self):
        incoming_data = request.get_json()
        data = User(
            username=incoming_data.get("username"),
            email=incoming_data.get("email"),
            password=incoming_data.get("password")
        )
        db.session.add(data)
        db.session.commit()

        response = {
            "message": "user created successfully",
            "data": data.to_dict()
        }
        return make_response(response, 201)
    
api.add_resource(UserResource, '/users')

class AssistanceResource(Resource):
    def get(self, id):
        associations = EmergencyResponse.query.filter_by(user_id=id).all()
        response_dict_list = [n.to_dict() for n in associations]
        return make_response(response_dict_list, 200)

    def post(self, id):
        incoming_data = request.get_json()

        # Debug print statement
        print("Incoming Data:", incoming_data)
        
        # Validation
        if not incoming_data.get("response_id"):
            return make_response({"message": "response_id is required"}, 400)
        
        data = EmergencyResponse(
            assistance_type=incoming_data.get("assistance_type"),
            user_id=id,
            response_id=incoming_data.get("response_id")
        )
        
        db.session.add(data)
        db.session.commit()
        
        response = {
            "message": "response created successfully",
            "data": data.to_dict()
        }
        return make_response(response, 201)

api.add_resource(AssistanceResource, '/assistance/<int:id>/assist')

if __name__ == "__main__":
    app.run(port=5555, debug=True)
