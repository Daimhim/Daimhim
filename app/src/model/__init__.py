# from app.src.model import ModelTools
# import app.src.model.BaseResponse as BaseResponse
# import json
# from django.core import serializers
#
#
# b = BaseResponse()
# b.error_msg = 'asfkljsad'
#
# print(json.dumps(ModelTools.object_to_json(b)))

from app.src.model.BaseResponse import BaseResponse
from app.src.model import ModelTools
BaseResponse = BaseResponse()
print(ModelTools.object_to_json(BaseResponse))