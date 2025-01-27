#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, EmergencyPost, Response
if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        print("Clearing database...")
        db.session.query(Response).delete()
        db.session.query(EmergencyPost).delete()
        db.session.query(User).delete()
        db.session.commit()
        users = []
        for i in range(10):
            user = User(
                username = fake.user_name(),
                email = fake.email(),
                password = fake.password(length=10)
            )
        users.append(user)
        db.session.add(user)
    db.session.commit()       

    posts = []
    for i in range(10): 
        post = EmergencyPost(
                location=fake.address(),
                type=rc(["Fire", "Medical", "Flood", "Accident", "Other"]),
                description=fake.text(max_nb_chars=200),
                date=fake.date_time_this_year(),
                user_id=rc([user.id for user in users])  # Assign a random user
        )
        posts.append(post)
        db.session.add(post)
    db.session.commit()
        
    for i in range(50):  
            response = Response(
                message=fake.sentence(),
                date=fake.date_time_this_month(),
                user_id=rc([user.id for user in users]),  
                post_id=rc([post.id for post in posts]) 
            )
            db.session.add(response)
    db.session.commit()

    print("Seeding completed successfully!")