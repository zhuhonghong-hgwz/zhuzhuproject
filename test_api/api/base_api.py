"""
封装requests和jsonpath等常用公共方法
"""
import requests
from jsonpath import jsonpath


class BaseApi:
    #传入一个参数，注释为字典形式
    def base_requests(self, req:dict):
        return requests.request(**req)

    def base_jsonpath(self, obj, json_expr):
        return jsonpath(obj, json_expr)