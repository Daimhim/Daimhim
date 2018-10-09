from django.db import models


# Create your models here.
class JokeModel(models.Model):
    hashId = models.CharField(max_length=35, unique=True)
    content = models.TextField()
    unixtime = models.IntegerField()
    updatetime = models.DateTimeField()
    url = models.ImageField()

# class ApkFileModerl(models.Model):
