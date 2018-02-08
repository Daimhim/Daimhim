from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("我就是主页，你敢信？")

