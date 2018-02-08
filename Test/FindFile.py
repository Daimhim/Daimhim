import os

filePath = "G:\MangoT5\TERA"
fileName = "Binaries"


def browser(path):
    if os.path.isdir(path):
        for root, dirs, list in os.walk(path):
            for i in list:
                if i in fileName:
                    print(os.path.join(root, i))
            for x in dirs:
                if x in fileName:
                    print(os.path.join(root, x))
    else:
        print(path)


browser(filePath)
