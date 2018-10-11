import json
import os
import re

from django.http import HttpResponse

import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import ApkFileModel as apkFile
from app.data import Passer as passer
APK_PATH = ''
APK_PATH_CACHE = ''
APK = ''
AAPT_PATH = ''


def __init__(self):
    self.APK_PATH = '../Daimhim/file/'
    self.APK_PATH_CACHE = '../Daimhim/Cache/'
    self.APK = '/apk/'
    self.AAPT_PATH = os.path.abspath(os.path.join(os.getcwd(), "..", 'data', 'aapt.exe'))


def upload(request):
    # request.encoding = 'utf-8'
    afmResponse = BaseResponse()
    afmResponse.error_code = 0
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        if user_id is None or user_id == '':
            afmResponse.error_msg = 'UserId can not empty'
            return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")
        file_ = request.FILES['file']
        if None is file_:
            afmResponse.error_msg = 'Please upload a file in apk format'
            return HttpResponse(jsonTool.object_to_json(afmResponse), "application/json")
        getAppBaseInfo(passer.save_cache_file(file_))
        # print(os.path.abspath(file_))
        # getAppBaseInfo(os.path.abspath(os.path.dirname(os.path.dirname(file_))))
        # filePath = save_apk_file(file_, app_name='', user_id=user_id)
        # apkFile.objects.create(userId=user_id, apk_name='', apk_url=filePath, app_version='')
        # apkFile.save()
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
    path = APK_PATH + jsonTool.str_to_md5(user_id) + '/' + jsonTool.str_to_md5(app_name) + APK
    if not os.path.exists(path):
        os.makedirs(path)  # 创建存储文件的文件夹
    destination = open(os.path.join(path, file.name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    pass


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
    output = os.popen(get_info_command).read()  # 执行命令，并将结果以字符串方式返回
    match = re.compile(
        "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'\\nsdkVersion:'(\S+)'\\ntargetSdkVersion:'(\S+)'").match(
        output)  # 通过正则匹配，获取包名，版本号，版本名称
    if not match:
        print(output)
        raise Exception("can't get packageinfo")
    return match
