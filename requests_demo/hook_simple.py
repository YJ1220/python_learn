#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
response:
从一个请求产生的响应
你可以通过传递一个 {hook_name: callback_function} 字典给 hooks 请求参数 为每个请求分配一个钩子函数：
hooks=dict(response=print_url)
callback_function 会接受一个数据块作为它的第一个参数。
def print_url(r, *args, **kwargs):
    print(r.url)
若执行你的回调函数期间发生错误，系统会给出一个警告。
若回调函数返回一个值，默认以该值替换传进来的数据。若函数未返回任何东西， 也没有什么其他的影响。
我们来在运行期间打印一些请求方法的参数：
requests.get('http://httpbin.org', hooks=dict(response=print_url))
http://httpbin.org
<Response [200]>
'''
import  requests

def get_key_info(response,*args,**kwargs):
    '''
    回调函数
    '''
    print(response.headers['Content-type'])

def main():
    '''
    主程序
    '''
    requests.get('https://api.github.com',hooks=dict(response=get_key_info))


if __name__ == "__main__":
    main()