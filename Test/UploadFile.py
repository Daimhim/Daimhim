# coding:utf-8
import os
import re as reTool;

path = "EditFile"


def getFileAndConcentrated():
    newFilePath = path + "//" + "newfile.txt"
    # if not os.path.exists(newFilePath):
    #     os.makedirs(path + "//" + "newfile.txt")
    with open(newFilePath, "w", encoding='UTF-8') as newFile:
        for fs in os.listdir(path):
            with open(path + "//" + fs, "r", encoding='UTF-8') as file:
                while 1:
                    print(type(file))
                    lines = file.readlines(100000)
                    if not lines:
                        break
                    for line in lines:
                        if line.startswith("####"):
                            newFile.writelines(line)


def documentClassification():
    gradeMap = {}
    with open(path + "//" + "newfile.txt", "r", encoding='UTF-8') as file:
        text = file.read()
        for s in text.split("####"):
            if s[2:3] == "-":
                subtitle_key = s[3:5].replace(" ", "")
                title_key = s[1:2].replace(" ", "")
                if not title_key in gradeMap:
                    #  没有key-value
                    gradeMap[title_key] = {subtitle_key: [s[5:len(s)]]}
                else:
                    if not subtitle_key in gradeMap.get(title_key):
                        gradeMap.get(title_key)[subtitle_key] = [s[5:len(s)]]
                    else:
                        gradeMap.get(title_key).get(subtitle_key).append(s[5:len(s)])
        return gradeMap


def typesetting(data):
    con = 0
    with open(path + "//" + "newfile2.txt", "w", encoding='UTF-8') as newFile:
        for i in data:
            title = ""
            if i == "1":
                title = "基本知识点/初中级"
            elif i == "2":
                title = "深入知识点/中高级"
            elif i == "3":
                title = "基本知识点的细节/高级"
            elif i == "4":
                title = "系统核心机制/高级、资深"
            elif i == "5":
                title = "琐碎的知识点/所有级别"
            else:
                title = "其它\n+  "
            print("title :" + title)
            newFile.write("####  " + title + "\n")
            for n in data.get(i):
                subtitle = ""
                if i == "1":
                    if n == "1":
                        subtitle = "四大组件"
                    elif n == "2":
                        subtitle = "如何布局"
                    elif n == "3":
                        subtitle = "自定义View"
                    elif n == "4":
                        subtitle = "动画等"
                    elif n == "5":
                        subtitle = "布局优化"
                    elif n == "6":
                        subtitle = "java基础"
                    elif n == "7":
                        subtitle = "适配"
                    elif n == "8":
                        subtitle = "序列化"
                    elif n == "9":
                        subtitle = "网络初级"
                    elif n == "10":
                        subtitle = "Android基础"
                    else:
                        pass
                elif i == "2":
                    if n == "1":
                        subtitle = "AIDL"
                    elif n == "2":
                        subtitle = "Binder"
                    elif n == "3":
                        subtitle = "多进程"
                    elif n == "4":
                        subtitle = "事件分发"
                    elif n == "5":
                        subtitle = "View系列"
                    elif n == "6":
                        subtitle = "消息队列"
                    elif n == "7":
                        subtitle = "动画细节"
                    elif n == "8":
                        subtitle = "性能优化"
                    elif n == "9":
                        subtitle = "设计模式"
                    elif n == "10":
                        subtitle = "数据结构"
                    elif n == "11":
                        subtitle = "线程"
                    elif n == "12":
                        subtitle = "第三方库"
                    elif n == "13":
                        subtitle = "网络"
                    else:
                        pass
                elif i == "3":
                    if n == "1":
                        subtitle = "Activity启动模式和标记位"
                    elif n == "2":
                        subtitle = "AsyncTask的版本演变"
                    elif n == "3":
                        subtitle = "Service的启动和绑定状态"
                    elif n == "4":
                        subtitle = "虚拟机深入了解"
                    elif n == "5":
                        subtitle = "插件化"
                    elif n == "6":
                        subtitle = "framework"
                    else:
                        pass
                elif i == "4":
                    if n == "1":
                        subtitle = "SystemServer的启动"
                    elif n == "2":
                        subtitle = "主线程的消息循环模型"
                    elif n == "3":
                        subtitle = "AMS和PMS"
                    elif n == "4":
                        subtitle = "Window和View的关系"
                    elif n == "5":
                        subtitle = "四大组件和AMS的交互"
                    else:
                        pass
                elif i == "5":
                    if n == "1":
                        subtitle = "如何打开一个网页"
                    elif n == "2":
                        subtitle = "如何打电话"
                    elif n == "3":
                        subtitle = "定位"
                    elif n == "4":
                        subtitle = "传感器"
                    elif n == "5":
                        subtitle = "AndroidStudio"
                    else:
                        pass
                else:
                    subtitle = "其它\n+  "
                # print("subtitle :" + subtitle)
                newFile.write("+  " + subtitle + "\n")
                for t in data.get(i).get(n):
                    # print("content " + t)
                    newFile.write(">+  " + t + "\n")
                    con = con + 1
    print(con)


def fileFilter(fileName):
    if fileName:
        if isinstance(fileName, str):
            return fileName\
                .replace('\\', '6')\
                .replace('/', '3')\
                .replace(':', '8')\
                .replace('：', '8')\
                .replace('?', '2')\
                .replace('？', '2')\
                .replace('<', '4')\
                .replace('>', '7')\
                .replace('*', '5')\
                .replace('\n', '')\
                .replace(' ', '')\
                .replace('|', '1')
    return fileName


def tidyDocument():
    with open(path + "//" + "newfile2.txt", "r", encoding='UTF-8') as file:
        line = file.readline()
        titlePath = ""
        subtitle = ""
        content = ""
        s = "####"
        prefix = "+"
        s1 = ">+"
        while line:
            if line.startswith(s):
                titlePath = path + "//" + fileFilter(line[len(s):len(line)])
                if not os.path.exists(titlePath):
                    os.makedirs(titlePath)
                    print(line)
            elif line.startswith(prefix):
                subtitle = titlePath + "//" + fileFilter(line[len(prefix):len(line)])
                if not os.path.exists(subtitle):
                    os.makedirs(subtitle)
                    print(line)
            elif line.startswith(s1):
                content = subtitle + "//" + fileFilter(line[len(s1):len(line)]) + ".md"
                with open(content, "w", encoding='UTF-8') as f:
                    f.writelines("####  必知：\n")
                    f.writelines("####  必会：")
            else:
                print(line)
            line = file.readline()


tidyDocument()
