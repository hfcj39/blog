from blog import db
from datetime import datetime


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    classification = db.Column(db.String, unique=True)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)

    comments = db.relationship('Article', backref='classes')
