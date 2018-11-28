from app import db


class Project(db.Model):
    name = db.Column(db.String(120), primary_key=True)


class EventBase(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String, db.ForeignKey('project.name'), nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'event',
        'polymorphic_on': type
    }


class PurchaseEvent(EventBase):
    __tablename__ = 'purchase_event'
    id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    customer_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'purchase_event',
    }


class ClickEvent(EventBase):
    __tablename__ = 'click_event'
    id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    track_id = db.Column(db.String(15))

    __mapper_args__ = {
        'polymorphic_identity': 'click_event',
    }
