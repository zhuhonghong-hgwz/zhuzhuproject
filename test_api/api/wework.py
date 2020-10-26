"""
WeWork独有的业务模块：获取token
"""
import requests

from test_api.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self, corp_secrect):
        corp_id = "ww524bcb5a02101a58"
        # corp_secrect = "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y"
        # get_token_url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        # r = requests.get(url=get_token_url)
        req={
            "method": "get",
            "url": f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        }
        r = self.base_requests(req)
        #定义一个公共属性供子类调用
        self.token=r.json()['access_token']
        #返回token值供其他方法调用
        return self.token