import json
import os
import re
import io

from django.http import HttpResponse

import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import ApkFileModel as apkFile
from app.data import Passer as passer
from app.src.model.models import UserModel as user


def upload(request):
    # request.encoding = 'utf-8'
    afmResponse = BaseResponse()
    afmResponse.error_code = 0
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        apk_name = request.POST.get('apkName')
        if user_id is None or user_id == '':
            afmResponse.error_msg = 'UserId can not empty'
            return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")
        file_ = request.FILES['file']
        if None is file_:
            afmResponse.error_msg = 'Please upload a file in apk format'
            return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")
        match = getAppBaseInfo(passer.save_cache_file(file_))
        package_name = match.group(1)
        version_code = match.group(2)
        version_name = match.group(3)
        sdk_version = match.group(4)
        target_sdk_version = match.group(5)
        if apk_name is None or apk_name == '':
            apk_name = jsonTool.str_to_md5(package_name)
        save_apk_file(file_, apk_name + '_' + version_code + '.apk', user_id)
        user_info = user.objects.get(userId=user_id)
        create = apkFile.objects.create(userId=user_info, apk_name=apk_name, apk_url='', sdk_version=sdk_version,
                                        target_sdk_version=target_sdk_version, version_code=version_code,
                                        version_name=version_name, package_name=package_name)
        create.save()
        afmResponse.error_msg = 'upload success'
        return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")
    else:
        afmResponse.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")


def get_apk_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('userId')
        if user_id is None or user_id == '':
            return HttpResponse("failure")
        path = APK_PATH + user_id + APK
        if not os.path.exists(path):
            os.makedirs(path)  # 创建存储文件的文件夹
        listdir = os.listdir(path)
        return HttpResponse(json.dumps(listdir, ensure_ascii=False), "application/json;")
    else:
        return HttpResponse("failure")


def get_last_apk(request):
    # 获取最新的apk
    pass


def save_apk_file(file, app_name, user_id):
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


def get_apk(userId, apkName):
    # 获取文件
    pass


def getAppBaseInfo(parm_apk_path):
    # packagename = match.group(1)
    # versionCode = match.group(2)
    # versionName = match.group(3)
    # sdkVersion = match.group(4)
    # targetSdkVersion = match.group(5)
    parm_aapt_path = passer.get_aapt()
    get_info_command = "%s dump badging %s" % (parm_aapt_path, parm_apk_path)
    popen = os.popen(get_info_command)
    popen = io.TextIOWrapper(popen.detach(), encoding='utf-8')
    output = popen.read()
    match = re.compile(
        "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'\\nsdkVersion:'(\S+)'\\ntargetSdkVersion:'(\S+)'").match(
        output)  # 通过正则匹配，获取包名，版本号，版本名称
    if not match:
        print(output)
        raise Exception("can't get packageinfo")
    return match
