
class BaseResponse:
    def __init__(self):
        self.error_code = 0
        self.error_msg = 'Request method error'
        self.result = None

    def obj2dir(self):
        return {"error_code": self.error_code, "error_msg": self.error_msg, "result": self.result}
