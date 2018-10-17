import os

from django.http import HttpResponse, StreamingHttpResponse

import app.src.model.ModelTools as jsonTool
from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import ApkFileModel
from app.src.model.models import PluginModel
from app.src.model.models import ApplicationModel

import uuid


def upload_apk(request):
    if request.method is 'POST':
        user_id = request.POST.get("userId")
        plugin_id = request.POST.get("pluginId")
        apk_name = request.POST.get("apkName")
        apk_url = request.POST.get("apkUrl")
        package_name = request.POST.get("packageName")
        version_code = request.POST.get("versionCode")
        version_name = request.POST.get("versionName")
        min_sdk_version = request.POST.get("minSdkVersion")
        target_sdk_version = request.POST.get("targetSdkVersion")
        apk_description = request.POST.get("apkDescription")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_name is None or apk_name == '':
            BaseResponse.error_msg = 'apk name can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_url is None or apk_url == '':
            BaseResponse.error_msg = 'apk url can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if package_name is None or package_name == '':
            BaseResponse.error_msg = 'package name can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if version_code is None or version_code == '':
            BaseResponse.error_msg = 'version code can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if version_name is None or version_name == '':
            BaseResponse.error_msg = 'version name can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if min_sdk_version is None or min_sdk_version == '':
            BaseResponse.error_msg = 'min sdk version can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if target_sdk_version is None or target_sdk_version == '':
            BaseResponse.error_msg = 'target sdk version can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_description is None or apk_description == '':
            BaseResponse.error_msg = 'apk description can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        plugin_model = PluginModel.objects.get(plugin_id=plugin_id)
        apk_file_model = ApkFileModel.objects.get(plugin_id=plugin_model, version_code=version_code)
        if apk_file_model is not None:
            BaseResponse.error_msg = 'current version already exists'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        apk_file = request.FILES['file']
        if apk_file is None:
            BaseResponse.error_msg = 'apk file can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        file_path = save_apk_file(apk_file, apk_name + '_' + version_code + '.apk',
                                  ApplicationModel.objects.get(app_id=plugin_model.app_id).user_id)
        apk_id = uuid.uuid1().__str__().replace('-', '')
        ApkFileModel.objects.create(plugin_id=plugin_model, apk_name=apk_name, apk_url=apk_url, apk_id=apk_id,
                                    package_name=package_name, version_code=version_code, version_name=version_name,
                                    min_sdk_version=min_sdk_version, target_sdk_version=target_sdk_version,
                                    apk_description=apk_description, apk_path=file_path).save()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'upload plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def update_apk(request):
    if request.method is 'PUT':
        user_id = request.PUT.get("userId")
        plugin_id = request.PUT.get("pluginId")
        apk_id = request.PUT.get("apkId")
        apk_url = request.PUT.get("apkUrl")
        min_sdk_version = request.PUT.get("minSdkVersion")
        target_sdk_version = request.PUT.get("targetSdkVersion")
        apk_description = request.PUT.get("apkDescription")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_id is None or apk_id == '':
            BaseResponse.error_msg = 'apk id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        apk_file_model = ApkFileModel.objects.get(plugin_id=PluginModel.objects.get(plugin_id=plugin_id), apk_id=apk_id)
        if target_sdk_version is not None and target_sdk_version != '':
            apk_file_model.objects.update(target_sdk_version=target_sdk_version)
        if apk_url is not None and apk_url != '':
            apk_file_model.objects.update(apk_url=apk_url)
        if apk_description is not None and apk_description != '':
            apk_file_model.objects.update(apk_description=apk_description)
        if min_sdk_version is not None and min_sdk_version != '':
            apk_file_model.objects.update(min_sdk_version=min_sdk_version)
        apk_file = request.FILES['file']
        if apk_file is None:
            BaseResponse.error_msg = 'apk file can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        file_path = save_apk_file(apk_file, apk_file_model.apk_name + '_' + apk_file_model.version_code + '.apk',
                                  ApplicationModel.objects.get(
                                      app_id=PluginModel.objects.get(plugin_id=plugin_id).app_id).user_id)
        apk_file_model.objects.update(apk_path=file_path)
        apk_file_model.save()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'update plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def delete_apk(request):
    if request.method == 'DELETE':
        plugin_id = request.DELETE.get("pluginId")
        apk_id = request.DELETE.get("apkId")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_id is None or apk_id == '':
            BaseResponse.error_msg = 'apk id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        ApkFileModel.objects.get(plugin_id=PluginModel.objects.get(plugin_id=plugin_id), apk_id=apk_id).delete()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'delete plugin success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_apk_list(request):
    if request.method is 'GET':
        user_id = request.POST.get("userId")
        plugin_id = request.POST.get("pluginId")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        BaseResponse.error_code = 1
        BaseResponse.result = ApkFileModel.objects.get(plugin_id=PluginModel.objects.get(plugin_id=plugin_id))
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def get_apk(request):
    if request.method is 'GET':
        user_id = request.POST.get("userId")
        plugin_id = request.POST.get("pluginId")
        apk_id = request.POST.get("apkId")
        if plugin_id is None or plugin_id == '':
            BaseResponse.error_msg = 'plugin id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if apk_id is None or apk_id == '':
            BaseResponse.error_msg = 'apk id can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        BaseResponse.error_code = 1
        BaseResponse.result = ApkFileModel.objects.get(plugin_id=PluginModel.objects.get(plugin_id=plugin_id),
                                                       apk_id=apk_id)
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def download_apk(request):
    if request.method is 'GET':
        apk_path = request.POST.get("apkPath")
        if apk_path is None or apk_path == '':
            BaseResponse.error_msg = 'apk path can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")

        def file_iterator(file_name, chunk_size=512):
            with open(file_name) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        join_path = os.path.join(get_project_path(), apk_path)
        response = StreamingHttpResponse(file_iterator(join_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(os.path.basename(join_path))
        return response
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def check_updates(request):
    if request.method is 'GET':
        pass
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def save_apk_file(file, app_name, user_id):
    #
    # 保存文件
    apk = os.path.join(jsonTool.str_to_md5(user_id), jsonTool.str_to_md5(app_name), 'apk')
    path = os.path.join(get_project_path(), 'file', apk)
    if not os.path.exists(path):
        os.makedirs(path)  # 创建存储文件的文件夹
    destination = open(os.path.join(path, app_name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return os.path.join(apk, app_name)


def get_project_path():
    return os.path.abspath(os.path.join(os.getcwd(), "."))
