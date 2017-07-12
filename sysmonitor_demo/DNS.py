#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# DNS域名轮询
# * [x] 实现域名的解析；获取域名所有的A记录解析IP列表
# * [x] 对IP列表进行HTTP级别的探测

import dns.resolver
import os
import  httplib2


iplist = [] #定义域名IP列表变量
appdomain = "www.google.com.hk"  #定义业务域名
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print("dns resolver eror:"+str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
