"""
具体业务：创建标签-更新标签名字-删除标签-获取标签列表
"""
import requests


class Tags():
    # 定义新建标签方法，并传入两个形参：token和tagid
    def creat_tags(self, token, tag_id):
        # 定义创建创建标签的url
        creat_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        # 定义请求体
        data = {
            "tagname": "标签1",
            "tagid": tag_id
        }
        # 根据接口文档说明，创建标签使用post请求,请求体使用Json数据格式
        r = requests.post(url=creat_tags_url, json=data)
        # return json格式的返回体
        return r.json()

    # 定义更新标签方法，并传入两个形参：token和tagid
    def update_tags(self, token, tag_id):
        upate_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        # 定义请求包体
        data = {
            "tagid": tag_id,
            "tagname": "更新后的标签"
        }
        r = requests.post(url=upate_tags_url, json=data)
        # return json格式的返回体
        return r.json()

    # 定义删除标签方法，并传入两个形参：token和tagid
    def delete_tags(self,token,tag_id):
        delete_tags_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tag_id}"
        r = requests.get(url=delete_tags_url)
        print(r.json())
        # return json格式的返回体
        return r.json()
    #定义获取标签列表的方法，并传入两个形参：token和tagid
    def get_tags_list(self,token,tag_id):
        # 定义获取列表的url
        get_tags_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}&tagid={tag_id}"
        # 发送获取列表请求
        list = requests.get(url=get_tags_list_url)
        return list.json()
