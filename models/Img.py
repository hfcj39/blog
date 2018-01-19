from blog import db
from datetime import datetime


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    path = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text)
    classification = db.column(db.String(16))
    visible = db.column(db.Integer)

    created_at = db.Column(db.DATETIME, default=datetime.utcnow())
    updated_at = db.Column(db.DATETIME, default=datetime.utcnow())
    delete_at = db.Column(db.DATETIME)
