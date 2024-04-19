class RatelimitedError(Exception):
    pass

class UnauthenticatedError(Exception):
    pass

class AuthenticationFailedError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)