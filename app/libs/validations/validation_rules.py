from app.libs.errors.validation_errors import RequiredPropertyNotFoundBadRequest, InvalidPropertyTypeBadRequest, \
    UnexpectedPropertyLenBadRequest


def required(data, property_name):
    if data is not None:
        return

    raise RequiredPropertyNotFoundBadRequest(property_name)


def of_type(expected_type):
    def type_validator(data, property_name):
        if isinstance(data, expected_type):
            return

        raise InvalidPropertyTypeBadRequest(property_name, expected_type, type(data))

    return type_validator


def of_len(min_len, max_len):
    def len_validator(data, property_name):
        if min_len <= len(data) <= max_len:
            return

        raise UnexpectedPropertyLenBadRequest(property_name, (min_len, max_len), len(data))

    return len_validator
