def required(data):
    return data is not None


def of_type(expected_type):
    def type_validator(data):
        return isinstance(data, expected_type)

    return type_validator


def is_valid(dict_schema, body, supports_extra=False):
    if not isinstance(dict_schema, dict):
        return False

    for field in dict_schema:
        data = body.get(field)

        for validator in dict_schema[field]:
            if not validator(data):
                return False

    if not supports_extra:
        return True

    for body_item in body:
        if body_item not in dict_schema:
            return False

    return True