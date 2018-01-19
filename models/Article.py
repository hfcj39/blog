from blog import db
from datetime import datetime


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.Text)
    classification = db.column(db.String(16))
    visible = db.column(db.Integer)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)

    comments = db.relationship('Comment', backref='article')
