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
    accountNumber = models.TextField(unique=True)
    upTime = models.DateTimeField(auto_now=True)
    crateTime = models.DateTimeField(auto_now_add=True)
    userName = models.TextField()
    passWord = models.TextField()
    userLogo = models.TextField()
    userPhone = models.TextField()
    userId = models.TextField(null=True, unique=True)
