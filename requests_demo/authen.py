#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])



def basic_auth():
    # 用户名密码认证
    auth=('user','password')
    response = requests.get(build_uri('user'),auth=auth)
    print(response.text)
    print(response.request.headers)

# base编码解码:在response.request.header信息中，可以发现返回Authorization的key值，对应的value是用Basic进行encode；所以可以对返回的值进行decode解码：
# 参考网站：https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001399413803339f4bbda5c01fc479cbea98b1387390748000
# import base64
# decode：解码
# base64.b64decode(字符串)

def token_auth():
    # token认证
    headers={'Authorization':'token e4b3f955f393ef2908ff8c1707719826488faf17'}
    response=requests.get(build_uri('user/emails'),headers=headers)
    print(response.headers)
    print(response.text)
    print(response.status_code)
    print(response.request.headers)


from requests.auth import  AuthBase

#调用requsts类的AuthBase


class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token = token

    def __call__(self,r):
        # 调用__call__函数，将类成为可调用的
        r.headers['Authorization'] = ' '.join(['token',self.token])
        return r

def auth_advanced():
    auth = GithubAuth('e4b3f955f393ef2908ff8c1707719826488faf17')
    response = requests.get(build_uri('user/emails'),auth=auth)
    print(response.text)


if __name__ == '__main__':
    auth_advanced()
