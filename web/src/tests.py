import os

from django.http import HttpResponse
from django.test import TestCase
from django.shortcuts import render


# Create your tests here.
def index(request):
    return render(request, "main.html")


def logo(request):
    d = os.path.abspath(os.path.join(__get_path(), os.path.pardir))
    image_path = os.path.join(d, "img/favicon.ico")
    imag_data = open(image_path, "rb").read()
    return HttpResponse(imag_data, content_type=r"image/ico")


def get_aapt():
    return os.path.join(__get_path(), 'aapt.exe')


def __get_path():
    return os.path.abspath(os.path.dirname(__file__))
