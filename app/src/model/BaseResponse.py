
class BaseResponse:
    def __init__(self):
        self.error_code = 0
        self.error_msg = 'Request method error'
        self.result = None

    def __str__(self) -> str:
        return {"error_code": self.error_code, "error_msg": self.error_msg, "result": self.result}.__str__()

    def obj2dir(self):
        return {"error_code": self.error_code, "error_msg": self.error_msg, "result": self.result}
