from app import db


class EventBase(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String, db.ForeignKey('project.name'), nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'event',
        'polymorphic_on': type
    }
