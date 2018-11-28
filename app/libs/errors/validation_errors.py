from werkzeug.exceptions import BadRequest


class RequiredPropertyNotFountBadRequest(BadRequest):
    def __init__(self, property_name):
        description = 'Required requests property "{property}" not found.'\
            .format(property=property_name)

        super().__init__(description)
        

class InvalidPropertyTypeBadRequest(BadRequest):
    def __init__(self, property_name, expected_type, found_type):
        description = 'Invalid type of property "{property}". ' \
                      'Expected \"{expected}\", but found \"{found}\"'\
            .format(property=property_name, expected=expected_type, found=found_type)

        super().__init__(description)


class UnexpectedPropertyLenBadRequest(BadRequest):
    def __init__(self, property_name, expected_len, found_len):
        description = 'Unexpected length of property "{property}". ' \
                      'Expected "{expected}", but found "{found}"'\
            .format(property=property_name, expected=expected_len, found=found_len)

        super().__init__(description)


class UnexpectedPropertyBadRequest(BadRequest):
    def __init__(self, property_name):
        description = 'Property "{property}" is not supported.' \
            .format(property=property_name)

        super().__init__(description)