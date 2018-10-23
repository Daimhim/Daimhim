from django.core.exceptions import FieldError
from django.db.utils import IntegrityError
from django.http import HttpResponse

from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import UserModel as mUser
import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
import uuid

BaseResponse = BaseResponse()


def user_login(request):
    # userLogin
    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username is None or username == '':
            BaseResponse.error_msg = 'username can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if password is None or password == '':
            BaseResponse.error_msg = 'password can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        from django.contrib.auth.models import Group
        try:
            user = mUser.objects.values('user_id', 'account_number', 'user_name', 'user_logo', 'user_phone',
                                        'pass_word').get(account_number=username)
        except FieldError:
            print(FieldError)
            BaseResponse.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        except mUser.DoesNotExist:
            BaseResponse.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if user is not None and user['pass_word'] != password:
            BaseResponse.error_msg = Error.Username_or_password_is_incorrect
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        BaseResponse.error_code = 1
        BaseResponse.error_msg = Error.Login_Success
        del user['pass_word']
        BaseResponse.result = user
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
    else:
        BaseResponse.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def user_registered(request):
    # userRegistered

    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username.strip() == '':
            BaseResponse.error_msg = Error.Registration_failed_UserName_empty
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        accountNumber = ''
        try:
            accountNumber = mUser.objects.get(accountNumber=username)
        except:
            pass
        if accountNumber is not None and accountNumber != '' and accountNumber.accountNumber != '' \
                and accountNumber.accountNumber == username:
            BaseResponse.error_msg = Error.Registration_failed_Cannot_register_repeatedly
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if password.strip() == '':
            BaseResponse.error_msg = Error.Registration_failed_password_empty
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        replace = uuid.uuid1().__str__().replace('-', '')
        try:
            mUser.objects.create(user_id=replace, account_number=username, pass_word=password).save()
        except IntegrityError:
            BaseResponse.error_msg = 'User already exists'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        BaseResponse.error_code = 1
        BaseResponse.error_msg = Error.Registered_Success
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
    else:
        BaseResponse.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")


def user_delete(request):
    if request.method is 'POST':
        user_id = request.POST.get('userId', '')
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username is None or username == '':
            BaseResponse.error_msg = 'username can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        if password is None or password == '':
            BaseResponse.error_msg = 'password can not be empty'
            return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
        mUser.objects.get(user_id=user_id, account_number=username, pass_word=password).delete()
        BaseResponse.error_code = 1
        BaseResponse.error_msg = 'delete user success'
    return HttpResponse(jsonTool.object_to_json(BaseResponse), "application/json")
