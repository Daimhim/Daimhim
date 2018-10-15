import app.src.model.Error as Error


class BaseResponse:
    def __init__(self):
        self.error_code = 0
        self.error_msg = Error.Request_method_error
        self.result = None



