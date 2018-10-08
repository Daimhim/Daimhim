from django.contrib import admin

# Register your models here.
import app.src.model.models as md

# 将models中创建的表添加到Django的admin中，用于进行后台操作
admin.site.register(md.JokeModel),