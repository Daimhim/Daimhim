import re
import requests

proxies = {"127.0.0.1:1081"}
respose = requests.get("https://m.cmdy555.com/")
respose.encoding = 'utf-8'
f = open('cmdy555.html', 'w', encoding='utf-8')
f.write(respose.text)
respose.close()
f.close()
