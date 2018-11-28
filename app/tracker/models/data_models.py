from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'
    name = Column(String(120), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Project: {name}>'.format(name=self.name)


class EventBase(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    project_name = Column(String, ForeignKey('project.name'), nullable=False)
    type = Column(String(50))
    project = relationship("Project", backref="events", lazy='joined')

    __mapper_args__ = {
        'polymorphic_identity': 'event',
        'polymorphic_on': type
    }

    def __init__(self, project):
        self.project = project

    def __repr__(self):
        return '<EventBase: project={project_name}>'.format(project_name=self.project.name)


class PurchaseEvent(EventBase):
    __tablename__ = 'purchase_event'
    id = Column(Integer, ForeignKey('event.id'), primary_key=True)
    customer_id = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'purchase_event',
    }

    def __init__(self, project, customer_id):
        super().__init__(project)
        self.customer_id = customer_id

    def __repr__(self):
        return '<PurchaseEvent: project={project_name}, customer_id={customer_id}>'\
            .format(project_name=self.project.name, customer_id=self.customer_id)


class ClickEvent(EventBase):
    __tablename__ = 'click_event'
    id = Column(Integer, ForeignKey('event.id'), primary_key=True)
    track_id = Column(String(15))

    __mapper_args__ = {
        'polymorphic_identity': 'click_event',
    }

    def __init__(self, project, track_id):
        super().__init__(project)
        self.track_id = track_id

    def __repr__(self):
        return '<ClickEvent: project={project_name}, track_id={track_id}>'\
            .format(project_name=self.project.name, track_id=self.track_id)
