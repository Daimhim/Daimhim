from django.core.exceptions import FieldError
from django.db.utils import IntegrityError
from django.http import HttpResponse

from app.src.model.BaseResponse import BaseResponse as BR
from app.src.model.models import UserModel as mUser
import app.src.model.Error as Error
import app.src.model.ModelTools as jsonTool
import uuid



def user_login(request):
    base_response = BR()
    # userLogin
    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username is None or username == '':
            base_response.error_msg = 'username can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        if password is None or password == '':
            base_response.error_msg = 'password can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        try:
            user = mUser.objects.values('user_id', 'account_number', 'user_name', 'user_logo', 'user_phone',
                                        'pass_word').get(account_number=username)
        except FieldError:
            print(FieldError)
            base_response.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        except mUser.DoesNotExist:
            base_response.error_msg = Error.Username_does_not_exist
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        if user is not None and user['pass_word'] != password:
            base_response.error_msg = Error.Username_or_password_is_incorrect
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        base_response.error_code = 1
        base_response.error_msg = Error.Login_Success
        del user['pass_word']
        base_response.result = user
        return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
    else:
        base_response.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.object_to_json(base_response), "application/json")


def user_registered(request):
    base_response = BR()
    # userRegistered
    if request.method == 'POST':
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username.strip() == '':
            base_response.error_msg = Error.Registration_failed_UserName_empty
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        account_number = ''
        try:
            account_number = mUser.objects.get(accountNumber=username)
        except:
            pass
        if account_number is not None and account_number != '' and account_number.accountNumber != '' \
                and account_number.accountNumber == username:
            base_response.error_msg = Error.Registration_failed_Cannot_register_repeatedly
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        if password.strip() == '':
            base_response.error_msg = Error.Registration_failed_password_empty
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        replace = uuid.uuid1().__str__().replace('-', '')
        try:
            mUser.objects.create(user_id=replace, account_number=username, pass_word=password).save()
        except IntegrityError:
            base_response.error_msg = 'User already exists'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        base_response.error_code = 1
        base_response.error_msg = Error.Registered_Success
        return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
    else:
        base_response.error_msg = Error.Request_method_error
        return HttpResponse(jsonTool.object_to_json(base_response), "application/json")


def user_delete(request):
    base_response = BR()
    if request.method is 'POST':
        user_id = request.POST.get('userId', '')
        username = request.POST.get('userName', '')
        password = request.POST.get('passWord', '')
        if username is None or username == '':
            base_response.error_msg = 'username can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        if password is None or password == '':
            base_response.error_msg = 'password can not be empty'
            return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
        mUser.objects.get(user_id=user_id, account_number=username, pass_word=password).delete()
        base_response.error_code = 1
        base_response.error_msg = 'delete user success'
    return HttpResponse(jsonTool.object_to_json(base_response), "application/json")
