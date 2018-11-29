from app.libs.errors.common_errors import InvalidUsage
from app.libs.errors.error_code import ErrorCode


class RequiredPropertyNotFoundBadRequest(InvalidUsage):
    def __init__(self, property_name):
        message = 'Required requests property "{property}" not found.' \
            .format(property=property_name)

        super().__init__(message, ErrorCode.REQUIRED_PROPERTY_NOT_FOUND)


class InvalidPropertyTypeBadRequest(InvalidUsage):
    def __init__(self, property_name, expected_type, found_type):
        message = 'Invalid type of property "{property}". ' \
                  'Expected "{expected}", but found "{found}"' \
            .format(property=property_name, expected=expected_type, found=found_type)

        super().__init__(message, ErrorCode.INVALID_PROPERTY_TYPE)


class UnexpectedPropertyLenBadRequest(InvalidUsage):
    def __init__(self, property_name, expected_len, found_len):
        message = 'Unexpected length of property "{property}". ' \
                  'Expected "{expected}", but found "{found}"' \
            .format(property=property_name, expected=expected_len, found=found_len)

        super().__init__(message, ErrorCode.UNEXPECTED_PROPERTY_LEN)


class UnexpectedPropertyValueBadRequest(InvalidUsage):
    def __init__(self, property_name, expected, found):
        message = 'Unexpected value of property "{property}". ' \
                  'Expected "{expected}", but found "{found}"' \
            .format(property=property_name, expected=expected, found=found)

        super().__init__(message, ErrorCode.UNEXPECTED_PROPERTY_VAL)


class UnexpectedPropertyBadRequest(InvalidUsage):
    def __init__(self, property_name):
        message = 'Property "{property}" is not supported.' \
            .format(property=property_name)

        super().__init__(message, ErrorCode.UNEXPECTED_PROPERTY)
