import pytest

from app import db, app
from app.tracker.models.data_models import EventBase, Project


@pytest.fixture
def client():
    with app.app_context():

        db.drop_all()
        db.create_all()

        create_initial_db_records()

        yield app.test_client()

        db.drop_all()


def create_initial_db_records():
    db.session.add(Project('acme'))
    db.session.add(Project('brain'))
    db.session.commit()
