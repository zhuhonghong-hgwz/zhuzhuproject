"""
WeWork独有的业务模块：获取token
"""
import requests


class WeWork():
    def get_token(self):
        corp_id = "ww524bcb5a02101a58"
        corp_secrect = "jfF4mymhHtk-b4kb7VmJ1vrlyBCnrqaeKpFx7t2oF6Y"
        get_token_url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secrect}"
        r = requests.get(url=get_token_url)
        #返回token值供其他方法调用
        return r.json()['access_token']