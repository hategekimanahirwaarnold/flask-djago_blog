#!/usr/bin/python3
from flaskBlog import app, db, User, Post

with app.app_context():
   user = User.query.all()
   print(user)
