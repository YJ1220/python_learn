#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 利用request下载和上传文件
import requests
URL = 'http://pic.58pic.com/58pic/16/38/45/03i58PICDKP_1024.jpg'
# 定制headers信息
headers = {'User-Agent':'Mozilla/5.0 (Macintos; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
def download_image_demo():
    # 获取原始相应内容；比如图片文本流文件；需要指定stream=True；
    # response.raw 所有的  response.raw(10) 前10个
    # 当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
    response = requests.get(URL,headers=headers,stream=True)

    # iter_content：一块一块的遍历要下载的内容
    # iter_lines：一行一行的遍历要下载的内容
    # 使用上面两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据。
    with open('down.jpg','wb') as fd:
        for chunk in response.iter_content(512):
            fd.write(chunk)

# 更好的一种方法，可以减少资源的消耗；
def download_image_imporved():
    '''
        demo:下载图片
    '''
    response = requests.get(URL,headers=headers,stream=True)
    from contextlib  import closing
    # 打开文件流后关闭
    with closing(requests.get(URL,stream=True)) as response:
    # 打开文件
        with open('down2.jpg', 'wb') as fd:
            for chunk in response.iter_content(512):
                fd.write(chunk)




if __name__ == "__main__" :
    print("执行函数")




