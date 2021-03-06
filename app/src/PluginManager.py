from app.src.model.BaseResponse import BaseResponse as BR
from django.http import HttpResponse
import app.src.model.ModelTools as jsonTool
from app.src.model.models import ApplicationModel
from app.src.model.models import PluginModel
import uuid


def register_plugin(request):
    BaseResponse = BR()
    # appId
    # pluginName
    # packageName
    if request.method == 'POST':
        app_id = request.POST.get("appId")
        plugin_name = request.POST.get("pluginName")
        package_name = request.POST.get("packageName")
        plugin_description = request.POST.get("pluginDescription")
        last_version_name = request.POST.get("versionName")
        last_version_code = request.POST.get("versionCode")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'app id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if plugin_name is None or plugin_name == '':
            BaseResponse.error_msg = 'plugin name can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if package_name is None or package_name == '':
            BaseResponse.error_msg = 'package name can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        plugin_id = uuid.uuid1().__str__().replace('-', '')
        application_model = ApplicationModel.objects.get(app_id=app_id)
        PluginModel.objects.create(plugin_id=plugin_id, app_id=application_model, plugin_name=plugin_name,
                                   package_name=package_name, plugin_description=plugin_description,
                                   last_version_name=last_version_name, last_version_code=last_version_code).save()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'register plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def update_plugin(request):
    pass


def delete_plugin(request):
    BaseResponse = BR()
    if request.method == 'DELETE':
        app_id = request.DELETE.get("appId")
        plugin_id = request.DELETE.get("pluginId")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'app id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        application_model = ApplicationModel.objects.get(app_id=app_id)
        PluginModel.objects.get(plugin_id=plugin_id, app_id=application_model).delete()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'delete plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_plugin_list(request):
    BaseResponse = BR()
    if request.method == 'GET':
        app_id = request.GET.get("appId")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'app id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        application_model = ApplicationModel.objects.get(app_id=app_id)
        plugin_models = PluginModel.objects.values(
            "plugin_id",
            "app_id",
            "plugin_name",
            "plugin_description",
            "package_name",
            "last_version_name",
            "last_version_code"
        ).filter(app_id=application_model)
        BaseResponse.result = {"list": list(plugin_models)}
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'request success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_plugin(request):
    BaseResponse = BR()
    if request.method == 'GET':
        app_id = request.GET.get("appId")
        plugin_id = request.GET.get("pluginId")
        if app_id is None or app_id == '':
            BaseResponse.error_msg = 'app id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        application_model = ApplicationModel.objects.get(app_id=app_id)
        BaseResponse.result = PluginModel.objects.get(plugin_id=plugin_id, app_id=application_model)
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'delete plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
