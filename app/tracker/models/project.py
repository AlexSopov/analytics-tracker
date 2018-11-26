from app import db


class Project(db.Model):
    name = db.Column(db.String(120), primary_key=True)