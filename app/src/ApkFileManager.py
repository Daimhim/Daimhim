from django.http import HttpResponse
import json as jsonTool
import os

APK_PATH = '../Daimhim/file/'
APK = '/apk/'


def upload(request):
    if request.method == 'POST':
        user_id = request.POST.get('userId')
        if user_id is None or user_id == '':
            return HttpResponse("failure")
        path = APK_PATH + user_id + APK
        if not os.path.exists(path):
            os.makedirs(path)  # 创建存储文件的文件夹
        file = request.FILES['file']
        destination = open(os.path.join(path, file.name), 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("success")
    else:
        return HttpResponse("failure")


def get_apk_list(request):
    if request.method == 'GET':
        user_id = request.GET.get('userId')
        if user_id is None or user_id == '':
            return HttpResponse("failure")
        path = APK_PATH + user_id + APK
        if not os.path.exists(path):
            os.makedirs(path)  # 创建存储文件的文件夹
        listdir = os.listdir(path)
        return HttpResponse(jsonTool.dumps(listdir, ensure_ascii=False), "application/json;")
    else:
        return HttpResponse("failure")

