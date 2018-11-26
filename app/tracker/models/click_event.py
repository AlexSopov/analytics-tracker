from app import db
from .event_base import EventBase


class ClickEvent(EventBase):
    __tablename__ = 'click_event'
    id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    track_id = db.Column(db.String(15))

    __mapper_args__ = {
        'polymorphic_identity': 'click_event',
    }
