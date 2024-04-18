class ErrorCodes:
    INVALID_ATTRIBUTE = 'Invalid attribute!'
    ENVIRONMENT_ERROR = 'Invalid environment!'
    API_KEY_ERROR = 'Invalid api key!'
    API_URL_ERROR = 'Invalid api url!'


class MetabaseException(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
