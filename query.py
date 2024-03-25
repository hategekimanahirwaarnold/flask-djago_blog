#!/usr/bin/python3
from flaskblog import app, db
from flaskblog.models import User, Post

with app.app_context():
   user = User.query.all()
   print(user)
