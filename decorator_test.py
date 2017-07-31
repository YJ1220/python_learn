#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
装饰器
'''

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



#decorator本身传入参数
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2017-3-35')


@log3('date')
def now3():
    print('2017-3-23')




now()
now3()