from app.libs.errors.validation_errors import UnexpectedPropertyBadRequest


def validate(dict_schema, body, supports_extra=False):
    for field in dict_schema:
        data = body.get(field)

        for validator in dict_schema[field]:
            validator(data, field)

    if supports_extra:
        return

    for body_item in body:
        if body_item not in dict_schema:
            raise UnexpectedPropertyBadRequest(body_item)

