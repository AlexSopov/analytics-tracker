from app import db
from app.tracker.models.data_models import PurchaseEvent, Project

project = Project('2')

for project in db.session.query(Project).all():
    if project.name is '2':
        print(project)
        b = project.events

        for event in b:
            print(event.project.name)
