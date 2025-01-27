from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import MetaData
from config import db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    emergency_posts = db.relationship('EmergencyPost', backref='user')
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

class EmergencyPost(db.Model):
    __tablename__ = "emergency_posts"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)  # Type of emergency (e.g., fire, flood)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    def __repr__(self):
        return (f"<EmergencyPost(id={self.id}, location='{self.location}', type='{self.type}', "
                f"description='{self.description}', date='{self.date}', user_id={self.user_id})>")
class Response(db.Model):
    __tablename__ = "responses"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("emergency_posts.id"), nullable=False)

    def __repr__(self):
        return (f"<Response(id={self.id}, message='{self.message}', date='{self.date}', "
                f"user_id={self.user_id}, post_id={self.post_id})>")