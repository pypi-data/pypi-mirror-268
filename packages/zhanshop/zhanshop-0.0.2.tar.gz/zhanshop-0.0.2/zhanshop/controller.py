import json

from flask import Response


class Controller():
    def result(data):
        if(isinstance(data, str) or isinstance(data, int)):
            return data
        else:
            response = Response(json.dumps(data, default=str, ensure_ascii=False))
            response.headers['Content-Type'] = "application/json; charset=utf-8"
            return response