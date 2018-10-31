import os

from django.http import HttpResponse, StreamingHttpResponse
from app.src.model.BaseResponse import BaseResponse
import app.src.model.ModelTools as jsonTool
from app.src.model.models import UserModel
from app.src.model.models import FileModel
from django.core.exceptions import FieldError
import app.src.model.Error as Error
import uuid


def up_load_file(request):
    base_response = BaseResponse()
    print(request.__dict__)
    if request.method == 'POST':
        user_id = request.POST.get("userId")
        print(user_id)
        if user_id is None or user_id == '':
            base_response.error_msg = 'user id can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        try:
            user = UserModel.objects.get(user_id=user_id)
        except FieldError:
            base_response.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        except UserModel.DoesNotExist:
            base_response.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        if user is None:
            base_response.error_msg = 'user id can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        apk_file = request.FILES['file']
        if apk_file is None:
            base_response.error_msg = 'file can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        replace = uuid.uuid1().__str__().replace('-', '')
        file_path = save_apk_file(apk_file, replace + '.png', user_id)
        file_model = FileModel.objects.create(user_id=UserModel.objects.get(user_id=user_id), serial_number=replace,
                                              file_path=file_path)
        file_model.save()
        base_response.result = {"file_id": file_model.serial_number}
        base_response.error_code = 1
        base_response.error_msg = 'upload image success'
    return HttpResponse(jsonTool.object_to_json(base_response), "application/json")


def get_file(request):
    base_response = BaseResponse()
    if request.method == 'GET':
        user_id = request.GET.get("userId")
        file_id = request.GET.get("fileId")
        file_model = FileModel.objects.get(user_id=UserModel.objects.get(user_id=user_id), serial_number=file_id)

        def file_iterator(file_name, chunk_size=512):
            with open(file_name, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        join_path = os.path.join(get_project_path(), file_model.file_path)
        response = StreamingHttpResponse(file_iterator(join_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(os.path.basename(join_path))
        return response
    return HttpResponse(jsonTool.object_to_json(base_response), "application/json")


def save_apk_file(file, file_name, user_id):
    #
    # 保存文件
    file_path = os.path.join(jsonTool.str_to_md5(user_id), 'img')
    path = os.path.join(get_project_path(), file_path)
    if not os.path.exists(path):
        os.makedirs(path)  # 创建存储文件的文件夹
    destination = open(os.path.join(path, file_name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return os.path.join(file_path, file_name)


def get_project_path():
    return os.path.abspath(os.path.join(os.path.join(os.getcwd(), "."), 'file'))
