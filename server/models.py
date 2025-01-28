from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from config import db  # Import the db from config

# Define your models here

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    emergency_posts = db.relationship('EmergencyPost', backref='user')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
class EmergencyPost(db.Model, SerializerMixin):
    __tablename__ = "emergency_posts"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)  # Type of emergency (e.g., fire, flood)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    responses = db.relationship('Response', backref='post')

    def __repr__(self):
        return (f"<EmergencyPost(id={self.id}, location='{self.location}', type='{self.type}', "
                f"description='{self.description}', date='{self.date}', user_id={self.user_id})>")
    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "type": self.type,
            "description": self.description,
            "date": self.date,
            "user_id": self.user_id
        }
class Response(db.Model, SerializerMixin):
    __tablename__ = "responses"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("emergency_posts.id"), nullable=False)
    #many to many relationship with user via emmergency response
    user = db.relationship('User', secondary='emergency_responses', backref='responses') 
    def __repr__(self):
        return (f"<Response(id={self.id}, message='{self.message}', date='{self.date}', "
                f"user_id={self.user_id}, post_id={self.post_id})>")

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "date": self.date,
            "user_id": self.user_id,
            "post_id": self.post_id
        }
# Many-to-Many Association Table
class EmergencyResponse(db.Model):
    __tablename__ = 'emergency_responses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    response_id = db.Column(db.Integer, db.ForeignKey('responses.id'), nullable=False)
    assistance_type = db.Column(db.String, nullable=False)  # e.g., medical aid, transport, etc.
    def __repr__(self):
        return (f"<EmergencyResponse(id={self.id}, user_id={self.user_id}, "
                f"response_id={self.response_id}, assistance_type='{self.assistance_type}')>")
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "response_id": self.response_id,
            "assistance_type": self.assistance_type
        }