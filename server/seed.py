#!/usr/bin/env python3

# Standard library imports
from random import choice as rc
# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, EmergencyPost, Response

# Initialize Faker
fake = Faker()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    print("Starting seed...")

    # Clear existing data from the database
    print("Clearing database...")
    db.session.query(Response).delete()
    db.session.query(EmergencyPost).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Seed Users
    print("Seeding users...")
    users = []
    for i in range(10):  # Create 10 users
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(length=10)
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()

    # Seeding Emergency Posts
    print("Seeding emergency posts...")
    posts = []
    for i in range(10):  # Create 10 emergency posts
        post = EmergencyPost(
            location=fake.address(),
            type=rc(["Fire", "Medical", "Flood", "Accident", "Other"]),
            description=fake.text(max_nb_chars=200),
            date=fake.date_time_this_year(),
            user_id=rc([user.id for user in users])
        )
        posts.append(post)
        db.session.add(post)
    db.session.commit()
    print("Seeding responses...")
    for i in range(50):  # Create 50 responses
        response = Response(
            message=fake.sentence(),
            date=fake.date_time_this_month(),
            user_id=rc([user.id for user in users]),  # random user ID
            post_id=rc([post.id for post in posts])  # random post ID
        )
        db.session.add(response)
    db.session.commit()

    print("Seeding completed successfully!")
