from sqlalchemy.dialects.postgresql import json

from app import db
from app.libs.errors.error_code import ErrorCode
from app.tracker.models.data_models import ClickEvent


def test_click_event_is_supported(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='click',
            data={
                'track_id': 'ABC123'
            }
        ))
    )

    assert response.status_code == 204


def test_click_event_is_added_to_db(client):

    assert db.session.query(ClickEvent)\
               .filter_by(track_id='ASD112233').count() == 0

    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='click',
            data={
                'track_id': 'ASD112233'
            }
        ))
    )

    assert response.status_code == 204

    added_event = db.session.query(ClickEvent)\
        .filter_by(track_id='ASD112233', project_name='acme')\
        .first()

    assert added_event is not None
    assert added_event.project_name == 'acme'
    assert added_event.track_id == 'ASD112233'


def test_invalid_track_id(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='click',
            data={
                'track_id': ''
            }
        ))
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.UNEXPECTED_PROPERTY_LEN
    assert 'track_id' in json_data.get('message')
