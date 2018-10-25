from django.db import models


# Create your models here.
# https://www.cnblogs.com/yangmv/p/5327477.html
class JokeModel(models.Model):
    hashId = models.CharField(max_length=35, unique=True)
    content = models.TextField()
    unixtime = models.IntegerField()
    updatetime = models.DateTimeField()
    url = models.ImageField()


class UserModel(models.Model):
    user_id = models.TextField(null=False, unique=True, primary_key=True)
    account_number = models.TextField(unique=True)
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    user_name = models.TextField()
    pass_word = models.TextField()
    user_logo = models.TextField()
    user_phone = models.TextField()


class ApplicationModel(models.Model):
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    app_id = models.TextField(null=False, unique=True, primary_key=True)
    app_name = models.TextField()
    app_url = models.TextField()
    app_logo = models.TextField()
    package_name = models.TextField()
    version_name = models.TextField()
    version_code = models.TextField()
    min_sdk_version = models.TextField()
    target_sdk_version = models.TextField()


class PluginModel(models.Model):
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    plugin_id = models.TextField(null=False, unique=True, primary_key=True)
    app_id = models.ForeignKey('ApplicationModel', on_delete=models.CASCADE)
    plugin_name = models.TextField()
    plugin_description = models.TextField()
    package_name = models.TextField()
    last_version_name = models.TextField()
    last_version_code = models.TextField()
    last_version_upTime = models.DateTimeField()
    models.IntegerField()
    models.IntegerField()


class ApkFileModel(models.Model):
    plugin_id = models.ForeignKey('PluginModel', on_delete=models.CASCADE)
    apk_id = models.TextField(null=False, unique=True, primary_key=True)
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    apk_name = models.TextField()
    apk_description = models.TextField()
    apk_url = models.TextField()
    apk_path = models.TextField()
    package_name = models.TextField()
    version_code = models.IntegerField(unique=True)
    version_name = models.TextField()
    min_sdk_version = models.IntegerField()
    target_sdk_version = models.IntegerField()
