from django.http import HttpRequest
from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import UserModel as mUser
import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
from django.http import HttpResponse


def register_app(request):
    if request.method == 'POST':
        user_id = request.POST.get("userId")
        app_name = request.POST.get("app_name")
        app_url = request.POST.get("app_url")
        app_logo = request.POST.get("app_logo")
        package_name = request.POST.get("package_name")
        if user_id is None or app_name == '':
            BaseResponse.error_msg = ''
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def delete_app(request):
    if request.method == 'DELETE':
        pass
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def update_app(request):
    if request.method == 'PUT':
        pass
    else:
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_app_list(request):
    if request.method == 'GET':
        pass
    else:
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_app(request):
    if request.method == 'GET':
        pass
    else:
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
