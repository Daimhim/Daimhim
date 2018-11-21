from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from Daimhim.settings import BASE_DIR as bs
import os


# Create your views here.


def index(request):
    print(bs)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    join_path = os.path.join(get_project_path(), "org.daimhim.plugin1_20181121151738.apk")
    response = StreamingHttpResponse(file_iterator(join_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(os.path.basename(join_path))
    return response


def get_project_path():
    return os.path.abspath(os.path.join(os.path.join(os.getcwd(), "."), 'file'))
