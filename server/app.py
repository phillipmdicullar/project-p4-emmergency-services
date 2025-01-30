#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from config import app, db
from models import User, EmergencyResponse, EmergencyPost, Response
from werkzeug.security import generate_password_hash, check_password_hash

# Configure JWT
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret key
jwt = JWTManager(app)

# Initialize API and Migrate
api = Api(app)
migrate = Migrate(app, db)

# Home Resource
class Home(Resource):
    def get(self):
        return make_response(jsonify({"message": "Welcome to Emergency Response API"}), 200)

api.add_resource(Home, '/')

# User Registration
class Register(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('username') or not data.get('email') or not data.get('password'):
            return make_response(jsonify({"error": "Missing username, email, or password"}), 400)

        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({"message": "User registered successfully"}), 201)

api.add_resource(Register, '/register')

# User Login
class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return make_response(jsonify({"error": "Missing username or password"}), 400)

        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity={'id': user.id})
            return make_response(jsonify(access_token=access_token), 200)
        return make_response(jsonify({"error": "Invalid username or password"}), 401)

api.add_resource(Login, '/login')

# EmergencyPost Resource
class EmergencyPostResource(Resource):
    @jwt_required()
    def get(self):
        try:
            posts = [post.to_dict() for post in EmergencyPost.query.all()]
            return make_response(jsonify(posts), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            if not data or not data.get('location') or not data.get('type') or not data.get('description'):
                return make_response(jsonify({"error": "Missing required fields"}), 400)

            new_post = EmergencyPost(**data)
            db.session.add(new_post)
            db.session.commit()
            return make_response(jsonify({"message": "Post created successfully", "data": new_post.to_dict()}), 201)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

api.add_resource(EmergencyPostResource, '/emergencies')

# EmergencyPost Detail Resource
class EmergencyPostDetailResource(Resource):
    @jwt_required()
    def get(self, id):
        try:
            post = EmergencyPost.query.get_or_404(id)
            return make_response(jsonify(post.to_dict()), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 404)

    @jwt_required()
    def put(self, id):
        try:
            data = request.get_json()
            post = EmergencyPost.query.get_or_404(id)
            for key, value in data.items():
                setattr(post, key, value)
            db.session.commit()
            return make_response(jsonify({"message": "Post updated successfully", "data": post.to_dict()}), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    @jwt_required()
    def delete(self, id):
        try:
            post = EmergencyPost.query.get_or_404(id)
            db.session.delete(post)
            db.session.commit()
            return make_response(jsonify({"message": "Post deleted successfully"}), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

api.add_resource(EmergencyPostDetailResource, '/emergencies/<int:id>')

# User Resource
class UserResource(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()['id']
            user = User.query.get_or_404(current_user_id)
            return make_response(jsonify(user.to_dict()), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 404)

api.add_resource(UserResource, '/user')

# Run the application
if __name__ == "__main__":
    app.run(port=5555, debug=True)