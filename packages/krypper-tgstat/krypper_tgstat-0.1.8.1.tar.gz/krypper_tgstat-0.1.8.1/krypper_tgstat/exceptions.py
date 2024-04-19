class TGStatException(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)


class TGStatTypeError(TGStatException):
    def __init__(self, get_type, need_type, var_name):
        self.message = f"The resulting type {get_type} does not match the type {need_type} in variable {var_name}"
        super().__init__(self.message)


class TGStatAPIError(TGStatException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class TGStatAuthError(TGStatException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)