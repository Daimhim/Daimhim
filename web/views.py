from django.http import HttpResponse
from django.shortcuts import render
from Daimhim.settings import BASE_DIR as bs
# Create your views here.


def index(request):
    print(bs)
    return render(request, 'templates/main.html', {})
    # return HttpResponse('nihao')

