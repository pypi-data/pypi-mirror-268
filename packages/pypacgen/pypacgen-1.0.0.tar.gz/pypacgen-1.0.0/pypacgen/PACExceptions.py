class PACException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidPACFunctionArgException(PACException):
    pass


class InvalidPACFileException(PACException):
    pass
