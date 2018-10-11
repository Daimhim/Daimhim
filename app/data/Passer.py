import os


def get_aapt():
    return os.path.join(__get_path(), 'aapt.exe')


def __get_path():
    return os.path.abspath(os.path.dirname(__file__))


def save_cache_file(file):
    path = os.path.join(__get_path(), 'cache')
    if not os.path.exists(path):
        os.makedirs(path)  # 创建存储文件的文件夹
    destination = open(os.path.join(path, file.name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()
    return os.path.abspath(os.path.join(path, file.name))
