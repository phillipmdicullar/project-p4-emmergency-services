from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from config import db  
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    # Relationships
    emergency_posts = db.relationship("EmergencyPost", back_populates="user", cascade="all, delete")
    emergency_responses = db.relationship("EmergencyResponse", back_populates="user", cascade="all, delete")

    # Association Proxy
    responses = association_proxy("emergency_responses", "response")

    # Password Hashing Methods
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

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
    type = db.Column(db.String(), nullable=False)  # e.g., fire, flood
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="emergency_posts")
    responses = db.relationship("Response", back_populates="post", cascade="all, delete")

    def __repr__(self):
        return (f"<EmergencyPost(id={self.id}, location='{self.location}', type='{self.type}', "
                f"description='{self.description}', date='{self.date}', user_id={self.user_id})>")

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "type": self.type,
            "description": self.description,
            "date": self.date.isoformat(),
            "user_id": self.user_id
        }


class Response(db.Model, SerializerMixin):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("emergency_posts.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    post = db.relationship("EmergencyPost", back_populates="responses")
    emergency_responses = db.relationship("EmergencyResponse", back_populates="response", cascade="all, delete")

    def __repr__(self):
        return (f"<Response(id={self.id}, message='{self.message}', date='{self.date}', "
                f"user_id={self.user_id}, post_id={self.post_id})>")

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "date": self.date.isoformat(),
            "user_id": self.user_id,
            "post_id": self.post_id
        }


# EmergencyResponse (Many-to-Many Relationship Model)
class EmergencyResponse(db.Model, SerializerMixin):
    __tablename__ = "emergency_responses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    response_id = db.Column(db.Integer, db.ForeignKey("responses.id", ondelete="CASCADE"), nullable=False)
    assistance_type = db.Column(db.String(), nullable=False)  # e.g., medical aid, transport, etc.

    # Relationships (Bidirectional)
    user = db.relationship("User", back_populates="emergency_responses")
    response = db.relationship("Response", back_populates="emergency_responses")

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
