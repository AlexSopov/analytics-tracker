from flask import jsonify


def no_content():
    response = jsonify(message='OK')
    response.status_code = 204

    return response
