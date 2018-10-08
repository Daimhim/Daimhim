import json as jsonTool


def objectToJson(objs):
    return jsonTool.dumps(objs, default=lambda obj: obj.__dict__)
