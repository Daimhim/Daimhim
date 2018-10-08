from urllib import request
from urllib import parse
import time
import json
import app.src.model.models as jm

appkey = "6a7f40ff902220aead73f5f746d423f1"
frequency = 100


def init(self):
    frequency = 100
    updatedJoke()


# https://www.juhe.cn/docs/api/id/95 接口文档
def updatedJoke():
    page = 1
    pagesize = 20
    params = parse.urlencode(
        {"page": page, "pagesize": pagesize, "key": appkey, "sort": "desc", "time": int(time.time())})
    f = request.urlopen("http://v.juhe.cn/joke/content/list.php?%s" % params)
    jsondata = json.loads(f.read().decode('utf-8'))
    print(jm.JokeModel.objects.all())
    # for n in jsondata['result']["data"]:
    #     print(n['hashId'])
    #     print(jm.JokeModel.objects.get_or_create(content=n['content'], hashId=n['hashId'], unixtime=n['unixtime'],
    #                                              updatetime=n['updatetime']))


def test():
    f = request.urlopen("http://127.0.0.1:8000/app/home/index/")
    print(json.loads(f.read().decode('utf-8')))
