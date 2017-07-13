# response的对象信息
<br>import requests
<br>URL = 'https://api.github.com'
<br>response = requests.get(URL)
## 查看response的帮助信息
`dir(response)`
## 具体使用：
* 状态码
<br>`response.status_code`
* 返回值
<br>`response.reason`
* 返回头部信息
<br>`response.headers`
<br>`response.headers['Server']` 查看返回头部某一值
* 请求的url
<br>`response.url`
* history 将http重定向到https
    <br>`response.history`
    <br>`[root@host ~]#:[ ]`
    <br>`response = requests.get('http://api.github.com')`
    <br>`response.history`
    <br>`[root@host ~]#:[response[301]]`
* 请求时间:
<br>`response.elapsed`
* requests请求方式:
<br>`response.requests`
* requests的headers:
<br>`response.requests.headers`
* 编码模式:
<br>`response.encoding`
* 查看返回信息:
    <br>`response.raw.read(100)` 前100
    <br>`response.content`
    <br>`response.text`
    <br>`response.json()`
    <br>`response.json()['team_url']`#查看其中team_url对应的值



