from urllib import request
from urllib import parse
import time
import json
import app.src.model.models as jm


def downliadFile():
    url = 'http://127.0.0.1:8000/app/home/getFile/?filename=web.txt'
    print("downloading with urllib")
    response = request.urlopen(url=url)
    # print(help(response))
    page = response.read()
    print(help(page))


appkey = "6a7f40ff902220aead73f5f746d423f1"


def request1(page=1, pagesize=20):
    params = parse.urlencode(
        {"sort": "desc", "page": page, "pagesize": pagesize, "time": int(time.time()), "key": appkey})
    f = request.urlopen("http://japi.juhe.cn/joke/content/list.from?%s" % params)
    decode = f.read().decode('utf-8')
    print(decode)
    print()
    print()
    print()
    jsondata = json.loads(decode)
    print(jsondata['result']["data"])
    for n in jsondata['result']["data"]:
        print(n['hashId'])
        print(jm.JokeModel.objects.get_or_create(content=n['content'], hashId=n['hashId'], unixtime=n['unixtime'],
                                                 updatetime=n['updatetime']))
    return decode


def request2(page=1, pagesize=20):
    params = parse.urlencode(
        {"page": page, "pagesize": pagesize, "key": appkey})
    f = request.urlopen("http://v.juhe.cn/joke/img/text.php?%s" % params)
    decode = f.read().decode('utf-8')
    print(decode)
    print()
    print()
    print()
    jsondata = json.loads(decode)
    print(jsondata['result']["data"])
    for n in jsondata['result']["data"]:
        print(n['hashId'])
        print(jm.JokeModel.objects.get_or_create(content=n['content'], hashId=n['hashId'], unixtime=n['unixtime'],
                                                 updatetime=n['updatetime'], url=n['url']))
    return decode
