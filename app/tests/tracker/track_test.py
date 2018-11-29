from flask import json

from app.libs.errors.error_code import ErrorCode


def test_nonexistent_project_returns_1001(client):
    response = client.post(
        '/track/nonexistent',
        data='{"event": "click", data: {} }'
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.PROJECT_DOES_NOT_EXIST
    assert 'nonexistent' in json_data.get('message')


def test_handle_invalid_json_with_1101(client):
    response = client.post(
        '/track/acme',
        data='{"event": "click",,, data: {} }'
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.JSON_LOADING_FAILED


def test_missing_event_value_returns_1102(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            data={},
        ))
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.REQUIRED_PROPERTY_NOT_FOUND
    assert 'event' in json_data.get('message')


def test_missing_data_value_returns_1102(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='click',
        ))
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.REQUIRED_PROPERTY_NOT_FOUND
    assert 'data' in json_data.get('message')


def test_invalid_data_type_returns_1103(client):
    response = client.post(
        '/track/acme',
        data=json.dumps(dict(
            event='click',
            data='100'
        ))
    )

    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data.get('code') == ErrorCode.INVALID_PROPERTY_TYPE
