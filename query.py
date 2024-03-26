#!/usr/bin/python3
from flaskblog import app, db
from flaskblog.models import User, Post

with app.app_context():
   posts = Post.query.paginate(per_page=5, page=2)
   for post in posts.items:
      print(f"{posts.page}, post: {post}")

