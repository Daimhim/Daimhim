import hashlib
import json as jsonTool


def object_to_json(objs):
    return jsonTool.dumps(objs, default=lambda obj: obj.__dict__)


def str_to_md5(content):
    return hashlib.md5(content.encode(encoding='utf-8')).hexdigest()
