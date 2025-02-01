from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from models import db, User, EmergencyPost, Response, EmergencyResponse
from config import app

# Initialize Flask extensions
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Ensure tables are created before the first request
@app.before_first_request
def create_tables():
    db.create_all()
@app.route('/')
def index():
    return "Default user home page"

# User Registration Endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password') or not data.get('email'):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({"message": "User registered successfully"}), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e)}), 500)

# User Login Endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'id': user.id, 'username': user.username})
        return make_response(jsonify({"access_token": access_token}), 200)

    return make_response(jsonify({"error": "Invalid username or password"}), 401)

# Get all Emergency Posts
@app.route('/emergencies', methods=['GET'])
@jwt_required()
def get_emergencies():
    posts = EmergencyPost.query.all()
    return make_response(jsonify([post.to_dict() for post in posts]), 200)

# Create an Emergency Post
@app.route('/emergencies', methods=['POST'])
@jwt_required()
def create_emergency():
    current_user = get_jwt_identity()
    data = request.get_json()

    if not data.get('type') or not data.get('location') or not data.get('description'):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    new_post = EmergencyPost(
        type=data['type'],
        location=data['location'],
        description=data['description'],
        user_id=current_user['id']
    )

    try:
        db.session.add(new_post)
        db.session.commit()
        return make_response(jsonify({"message": "Emergency Post created", "post": new_post.to_dict()}), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e)}), 500)

# Edit an Emergency Post
@app.route('/emergencies/<int:id>', methods=['PUT'])
@jwt_required()
def update_emergency(id):
    current_user = get_jwt_identity()
    post = EmergencyPost.query.get_or_404(id)

    if post.user_id != current_user['id']:
        return make_response(jsonify({"error": "Unauthorized to edit this post"}), 403)

    data = request.get_json()
    post.type = data.get('type', post.type)
    post.location = data.get('location', post.location)
    post.description = data.get('description', post.description)

    try:
        db.session.commit()
        return make_response(jsonify({"message": "Post updated", "post": post.to_dict()}), 200)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e)}), 500)

# Delete an Emergency Post
@app.route('/emergencies/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_emergency(id):
    current_user = get_jwt_identity()
    post = EmergencyPost.query.get_or_404(id)

    if post.user_id != current_user['id']:
        return make_response(jsonify({"error": "Unauthorized to delete this post"}), 403)

    try:
        db.session.delete(post)
        db.session.commit()
        return make_response(jsonify({"message": "Post deleted"}), 200)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e)}), 500)

# Add Response to Emergency Post
@app.route('/emergencies/<int:post_id>/responses', methods=['POST'])
@jwt_required()
def add_response(post_id):
    current_user = get_jwt_identity()

    post = EmergencyPost.query.get_or_404(post_id)

    data = request.get_json()
    response_text = data.get('response')

    if not response_text:
        return make_response(jsonify({"error": "Response text is required"}), 400)

    new_response = Response(
        message=response_text,
        user_id=current_user['id'],
        post_id=post.id
    )

    try:
        db.session.add(new_response)
        db.session.commit()
        return make_response(jsonify({"message": "Response added", "response": new_response.to_dict()}), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"error": str(e)}), 500)


if __name__ == '__main__':
    app.run(debug=True)
