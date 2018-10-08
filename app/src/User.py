from django.http import HttpResponse
from app.src.model.BaseResponse import BaseResponse
from app.src.model.models import UserModel as mUser
import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
import uuid


def userLogin(request):
    # userLogin
    mBaseResponse = BaseResponse()
    mBaseResponse.error_code = 0
    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        user = None
        try:
            user = mUser.objects.get(accountNumber=username)
        except:
            pass
        if user is None:
            mBaseResponse.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
        if user is not None and user.passWord != password:
            mBaseResponse.error_msg = Error.Username_or_password_is_incorrect
            return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
        mBaseResponse.error_code = 1
        mBaseResponse.error_msg = Error.Login_Success
        return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
    else:
        mBaseResponse.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")


def userRegistered(request):
    # userRegistered
    mBaseResponse = BaseResponse()
    mBaseResponse.error_code = 0
    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username.strip() == '':
            mBaseResponse.error_msg = Error.Registration_failed_UserName_empty
            return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
        accountNumber = ''
        try:
            accountNumber = mUser.objects.get(accountNumber=username)
        except:
            pass
        if accountNumber is not None and accountNumber != '' and accountNumber.accountNumber != '' \
                and accountNumber.accountNumber == username:
            mBaseResponse.error_msg = Error.Registration_failed_Cannot_register_repeatedly
            return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
        if password.strip() == '':
            mBaseResponse.error_msg = Error.Registration_failed_password_empty
            return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
        replace = uuid.uuid1().__str__().replace('-', '')
        create = mUser.objects.create(userId=replace, accountNumber=username, passWord=password)
        create.save()
        print(type(create))
        mBaseResponse.error_code = 1
        mBaseResponse.error_msg = Error.Registered_Success
        return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
    else:
        mBaseResponse.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.objectToJson(mBaseResponse), "application/json")
