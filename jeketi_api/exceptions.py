import logging

logger = logging.getLogger(__name__)

class ClientError(Exception):
    """Generic error class, catch-all for most client issues.
    """
    def __init__(self, msg, code=None, error_response=''):
        self.code = code or 0
        self.error_response = error_response
        super(ClientError, self).__init__(msg)

class ClientLoginError(ClientError):
    """Raised when login fails."""
    pass