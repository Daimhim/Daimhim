import hashlib
import json
from django.core import serializers
import pickle


def object_to_json(objs):
    if objs is None or objs == '':
        raise RuntimeError("objs can not be empty")
    dumps = json.dumps(objs, default=lambda obj: obj.__dict__)
    print(dumps)
    return dumps


def str_to_md5(content):
    return hashlib.md5(content.encode(encoding='utf-8')).hexdigest()
