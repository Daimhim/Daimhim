from wsgiref.util import FileWrapper

from django import forms
from django.http import HttpResponse
import json as jsonTool
import os
import app.src.test.DownloadFile as df
import app.src.model.models as modelsTool
from django.core import serializers as serializersTool

# Create your views here.


def index(request):
    print(request.path)
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(jsonTool.dumps(resp), "application/json")


def testPost(request):
    if request.method == 'POST':
        resp = {'errorcode': 200, 'detail': 'Get success', 'data': [1, 2, 3, 4, 5, 6, 8, 7, 9]}
        return HttpResponse(jsonTool.dumps(resp), "application/json")
    else:
        return HttpResponse("404")


def upLoadFiles(request):
    print(request.method)
    if request.method == "POST":
        # form = UploadFileForm(request.POST, request.FILES)
        path = 'F:\\PycharmProjects\\Daimhim\\app\\log'  # 创建文件存储路径
        if not os.path.exists(path):
            os.makedirs(path)  # 创建存储文件的文件夹
        # print(form.title)
        # print(form.is_valid())
        # if form.is_valid():
        file = request.FILES['file']
        destination = open(os.path.join(path, file.name), 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse('/success/url/')
        # else:
        #     return HttpResponse('Storage failure')
    else:
        return HttpResponse("success")


def getFile(request):
    get = request.GET.get('filename')
    # print("没有文件名："+get)
    if request.method == 'GET' and None != get:
        print(request)
        file_path = os.getcwd() + '\\app\\data\\' + get
        response = HttpResponse(FileWrapper(open(file_path, 'rb')))
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=%s' % get
        return response
    else:
        return HttpResponse("你哪里错了？")


def testForward(request):
    page = request.GET.get('page')
    pagesize = request.GET.get('pagesize')
    return HttpResponse(df.request2(page, pagesize))


def getJokeList(request):
    JokeModerate = modelsTool.JokeModel.objects.all()
    serialize = serializersTool.serialize('json', JokeModerate)
    return HttpResponse(jsonTool.dumps({"error_code": 0, "reason": "Success", 'data': serialize}), "application/json")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
