from app.lib.validations.validation_rules import required, of_type, of_len
from app.lib.validations.validators import is_valid


def track_schema():
    return {
        'event': [required, of_type(str)],
        'data': [required, of_type(dict)],
    }


def click_data_schema():
    return {
        'track_id': [required, of_type(str), of_len(5, 15)],
    }


def purchase_data_schema():
    return {
        'customer_id': [required, of_type(int)],
    }
