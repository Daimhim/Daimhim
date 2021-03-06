from django.http import HttpRequest
from app.src.model.BaseResponse import BaseResponse as BR
from app.src.model.models import UserModel as mUser
from app.src.model.models import ApplicationModel as application
import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
from django.http import HttpResponse
import uuid


def register_app(request):
    BaseResponse = BR()
    if request.method == 'POST':
        user_id = request.POST.get("userId")
        app_name = request.POST.get("appName")
        app_url = request.POST.get("appUrl")
        app_logo = request.POST.get("appLogo")
        package_name = request.POST.get("packageName")
        version_name = request.POST.get("versionName")
        version_code = request.POST.get("versionCode")
        min_sdk_version = request.POST.get("minSdkVersion")
        target_sdk_version = request.POST.get("targetSdkVersion")
        if user_id is None or user_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_name is None or app_name == '':
            BaseResponse.error_msg = 'appName can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_url is None or app_url == '':
            BaseResponse.error_msg = 'appUrl can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_logo is None or app_logo == '':
            BaseResponse.error_msg = 'appLogo can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if package_name is None or package_name == '':
            BaseResponse.error_msg = 'packageName can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        try:
            user_model = mUser.objects.get(user_id=user_id)
        except mUser.DoesNotExist:
            BaseResponse.error_msg = 'packageName can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        app_id = uuid.uuid1().__str__().replace('-', '')
        application.objects.create(user_id=user_model, app_id=app_id, app_name=app_name, app_url=app_url,
                                   app_logo=app_logo, package_name=package_name, version_name=version_name,
                                   version_code=version_code, min_sdk_version=min_sdk_version,
                                   target_sdk_version=target_sdk_version).save()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'register app success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def delete_app(request):
    BaseResponse = BR()
    if request.method == 'DELETE':
        user_id = request.DELETE.get("userId")
        app_id = request.DELETE.get("appId")
        if user_id is None or user_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        application.objects.get(app_id=app_id).delete()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'delete app success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def update_app(request):
    BaseResponse = BR()
    if request.method == 'PUT':
        user_id = request.PUT.get("userId")
        app_id = request.PUT.get("appId")
        app_name = request.PUT.get("appName")
        app_url = request.PUT.get("appUrl")
        app_logo = request.PUT.get("appLogo")
        package_name = request.PUT.get("packageName")
        version_name = request.POST.get("versionName")
        version_code = request.POST.get("versionCode")
        min_sdk_version = request.POST.get("minSdkVersion")
        target_sdk_version = request.POST.get("targetSdkVersion")
        if user_id is None or user_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'appId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        user_model = mUser.objects.get(userId=user_id)
        app_model = application.objects.get(user_id=user_model, app_id=app_id)
        if app_name is not None and app_name != '':
            app_model.objects.update(app_name=app_name)
        if app_url is not None and app_url != '':
            app_model.objects.update(app_url=app_url)
        if app_logo is not None and app_logo != '':
            app_model.objects.update(app_logo=app_logo)
        if package_name is not None and package_name != '':
            app_model.objects.update(package_name=package_name)
        if version_name is not None and version_name != '':
            app_model.objects.update(version_name=version_name)
        if version_code is not None and version_code != '':
            app_model.objects.update(version_code=version_code)
        if min_sdk_version is not None and min_sdk_version != '':
            app_model.objects.update(min_sdk_version=min_sdk_version)
        if target_sdk_version is not None and target_sdk_version != '':
            app_model.objects.update(target_sdk_version=target_sdk_version)
        app_model.save()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'update app success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_app_list(request):
    BaseResponse = BR()
    print(request.path)
    print(request.get_host())
    if request.method == 'GET':
        user_id = request.GET.get("userId")
        if user_id is None or user_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        user_model = mUser.objects.get(user_id=user_id)
        app_model = application.objects.values(
            'user_id',
            'app_id',
            'app_name',
            'app_url',
            'app_logo',
            'package_name',
            'version_name',
            'version_code',
            'min_sdk_version',
            'target_sdk_version',
        ).filter(user_id=user_model)
        BaseResponse.result = {"list": list(app_model)}
        BaseResponse.error_code = '1'
        BaseResponse.error_msg = ''
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_app(request):
    BaseResponse = BR()
    if request.method == 'GET':
        user_id = request.GET.get("userId")
        app_id = request.GET.get("appId")
        if user_id is None or user_id == '':
            BaseResponse.error_msg = 'userId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'appId can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        user_model = mUser.objects.get(userId=user_id)
        app_model = application.objects.get(userId=user_model, app_id=app_id)
        BaseResponse.result = app_model
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
