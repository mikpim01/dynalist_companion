from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    browser_pushid = db.Column(db.Text, nullable=True)
    push_email = db.Column(db.Integer, nullable=True, default='1')
    push_web = db.Column(db.Integer, nullable=True, default='1')