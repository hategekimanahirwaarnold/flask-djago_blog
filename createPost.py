#!/usr/bin/python3
from flaskblog import app, db
from flaskblog.models import User, Post

with app.app_context():
    post1 = Post(title='blog 1', content='First Post content!', user_id = 1)
    post2 = Post(title='blog 2', content='Second Post content!', user_id = 1)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
