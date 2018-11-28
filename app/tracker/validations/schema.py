from app.lib.validations.validation_rules import required, of_type
from app.lib.validations.validators import is_valid


def track_schema():
    return {
        'event': [required, of_type(str)],
        'data': [required, of_type(dict)],
    }


def click_data_schema():
    return {
        'track_id': [required, of_type(str)],
    }


def purchase_data_schema():
    return {
        'customer_id': [required, of_type(int)],
    }
