#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import json
import requests
URL = 'https://api.github.com'
# https://developer.github.com/v3/users/
# gitHub-API操作

#uri拼接
def build_uri(endpoint):
    return '/'.join([URL,endpoint])
#输出json格式化
def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)
 #查询账号信息
def requests_users():
    response = requests.get(build_uri('users/YJ1220'))
    #print(response.text)
    print(better_print(response.text))

#查询email信息
def requests_method():
    response = requests.get(build_uri('user/emails'),auth=('user','passwd') )
    print(better_print(response.text))

def params_requests():
    #查看前10的用户
    response = requests.get(build_uri('users'),params={'since':11})
    print(better_print(response.text))
    #请求的头部信息
    print(response.request.headers)
    #请求的url
    print(response.request.url)

def json_requests():
    #添加邮件post 删除邮件DELETE
    response = requests.delete(build_uri('user/emails'),auth=('user','passwd'),json=[ 'helloworld@github.com'] )
    #修改用户信息
    #response = requests.patch(build_uri('user'),auth=('user','passwd'),json={'company':'private enterprises','bio':'USER'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

#requests 异常检查
def timeout_requests():
    try:
        response = requests.get(build_uri('users/YJ1220'),timeout=10)
        # response = requests.get(build_url('user/emails'),timeout=0.1)
        response.raise_for_status()
    #超时
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    #http返回了不成功的状态码；需要指定response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
    #超过了设定的最大重定向次数
    except requests.exceptions.TooManyRedirects as e:
        print(e)
    #所有Requests显式抛出的异常
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(better_print(response.text))
        print(response.status_code )


#自定义request
def custom_requests():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'fask1.3.4'}
    req = Request('GET',build_uri('user/emails'),auth=('user','passwd'),headers=headers)
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp = s.send(prepped,timeout=5)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)
s


if __name__ == '__main__':

