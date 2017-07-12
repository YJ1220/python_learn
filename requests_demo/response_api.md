# response的对象信息

import requests
URL = 'https://api.github.com'
response = requests.get(URL)

# 查看response的帮助信息
    dir(response)

# 具体使用：
## 状态码
    response.status_code
## 返回值
    response.reason
## 返回头部信息
    response.headers
## 请求的url
    response.url
## history 将http重定向到https
    response.history
    >>>[]
    response = requests.get('http://api.github.com')
    response.history
    >>>[response[301]]
## 请求时间
    response.elapsed
## requests请求方式
    response.requests
* requests的headers
    response.requests.headers
* 编码模式
    response.encoding
## 查看返回信息
    response.raw.read(100) #前100行
    response.content
    response.text
    response.json()
    response.json()['team_url']



