#!/usr/bin/python3
from flaskblog import app, db, User, Post

with app.app_context():
    user1 = User(username="hirwa", email="hirwa@gmail.com", password="password")
    db.session.add(user1)
    db.session.commit()
