#!/usr/bin/env python3

# Remote library imports
from flask import Flask
from flask_migrate import Migrate
from config import app, db, api
from models import User, EmergencyPost, Response

# App configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Run the application
if __name__ == "__main__":
    app.run(port=5555, debug=True)
