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
    userId = models.TextField(null=False, unique=True, primary_key=True)
    accountNumber = models.TextField(unique=True)
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    userName = models.TextField()
    passWord = models.TextField()
    userLogo = models.TextField()
    userPhone = models.TextField()


class ApkFileModel(models.Model):
    userId = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    apk_name = models.TextField()
    apk_url = models.TextField()
    package_name = models.TextField()
    version_code = models.IntegerField()
    version_name = models.TextField()
    sdkVersion = models.IntegerField()
    targetSdkVersion = models.IntegerField()
