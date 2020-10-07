from .db import db

class Challenges(db.Document):
    title = db.StringField(required=True, unique=True)
    description = db.ListField(db.StringField(), required=True)
    time = db.ListField(db.StringField(), required=True)