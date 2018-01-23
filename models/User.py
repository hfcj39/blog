from blog import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)

    articles = db.relationship('Article', backref='user')
