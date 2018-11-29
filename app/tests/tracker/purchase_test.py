from sqlalchemy.dialects.postgresql import json

from app import db
from app.libs.errors.error_code import ErrorCode
from app.tracker.models.data_models import ClickEvent, PurchaseEvent


def test_purchase_event_is_supported(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='purchase',
            data={
                'customer_id': 1231123
            }
        ))
    )

    assert response.status_code == 204


def test_purchase_event_is_added_to_db(client):
    customer_id = 323112231
    project_name = 'acme'

    assert db.session.query(PurchaseEvent)\
               .filter_by(customer_id=customer_id).count() == 0

    response = client.post(
        '/track/{project}'.format(project=project_name),
        data=json.dumps(dict(
            event='purchase',
            data={
                'customer_id': customer_id
            }
        ))
    )

    assert response.status_code == 204

    added_event = db.session.query(PurchaseEvent)\
        .filter_by(customer_id=customer_id, project_name=project_name)\
        .first()

    assert added_event is not None
    assert added_event.project_name == project_name
    assert added_event.customer_id == customer_id


def test_invalid_customer_id(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='purchase',
            data={
                'customer_id': -100
            }
        ))
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.UNEXPECTED_PROPERTY_VAL
    assert 'customer_id' in json_data.get('message')
