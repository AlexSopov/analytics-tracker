from app import db
from .event_base import EventBase


class PurchaseEvent(EventBase):
    __tablename__ = 'purchase_event'
    id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    customer_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'purchase_event',
    }
