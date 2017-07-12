#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET= 'http://httpbin.org/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print("'>>>Response Headers:'")
    print(response.headers)
    print("'>>>Status Code:'")
    print(response.status_code)
    print("'>>>Respose Body:'")
    print(response.text)

def use_params_requests():
    params = {'param1':'hello','param2':'world'}
    #发送请求
    response = requests.get(URL_IP,params=params)
    #处理相应
    print("'>>>Response Headers:'")
    print(response.headers)
    print("'>>>Status Code:'")
    print(response.status_code)
    print(response.reason)
    print("'>>>Respose Body:'")
    print(response.json())



if __name__ == "__main__":
    print('use_simple_requests:')
    use_simple_requests()
    print('##########################################')
    print('use_params_requests')
    use_params_requests()
