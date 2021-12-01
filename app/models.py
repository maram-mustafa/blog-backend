from app import db
from datetime import datetime


# step1: create model in database
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posted_by = db.Column(db.String(64), index=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(64))
    date = db.Column(db.DateTime, default=datetime.utcnow())
    image = db.Column(db.String)

    def __init__(self, posted_by, title, body, image):
        self.posted_by = posted_by
        self.title = title
        self.body = body
        self.image = image
