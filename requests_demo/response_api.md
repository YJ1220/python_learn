# response的对象信息
import requests  
URL = 'https://api.github.com'  
response = requests.get(URL)
## 查看response的帮助信息
`dir(response)`
## 具体使用：
* 状态码
`response.status_code`
* 返回值
`response.reason`
* 返回头部信息
<br>`response.headers`
<br>`response.headers['Server']`#查看返回头部某一值
* 请求的url
`response.url`
* history 将http重定向到https
    <br>`response.history`</br>
    <br>`[root@host ~]#:[ ]`</br>
    <br>`response = requests.get('http://api.github.com')`</br>
    <br>`response.history`</br>
    <br>`[root@host ~]#:[response[301]]`</br>
* 请求时间:
`response.elapsed`
* requests请求方式:
`response.requests`
* requests的headers:
`response.requests.headers`
* 编码模式:
`response.encoding`
* 查看返回信息:
    <br>`response.raw.read(100)` #前100 </br>
    <br>`response.content` </br>
    <br>`response.text` </br>
    <br>`response.json()` </br>
    <br>`response.json()['team_url']`#查看其中team_url对应的值



