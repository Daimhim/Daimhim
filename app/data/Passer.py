import os


def get_aapt():
    return os.path.join(__get_path(), 'data', 'aapt.exe')


def __get_path():
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
