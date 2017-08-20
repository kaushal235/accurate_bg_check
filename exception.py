class BaseException(Exception):
    pass


class ValidationException(BaseException):

    def __init__(self, message, errors):
        super(ValidationException, self).__init__(message)
        self.errors = errors
