from urllib import request

url = 'http://127.0.0.1:8000/app/home/getFile/?filename=web.txt'
print("downloading with urllib")
response  = request.urlopen(url=url)
# print(help(response))
page = response.read()
print(help(page))
# print(str(page, encoding='utf-16'))