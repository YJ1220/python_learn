#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 第一天
## 使用while循环输入 1 2 3 4 5 6     8 9 10
i = 0
while True:
    i = i + 1
    if i == 7 :
        continue
    if i > 10:
        break
    print(i)

## 求1-100的所有数的和
from functools import reduce
sum = reduce(lambda x,y:x+y,range(101) )
print(sum)


sum = 0
for i in range(101):
    sum = sum + i

print(sum)

## 输出 1-100 内的所有奇数和偶数
even_num=[]
odd_num=[]
for i in range(1,101):
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)


## 求1-2+3-4+5 ... 99的所有数的和
sum = 0
for i in range(1,100):
    if i % 2 == 1:
        sum = sum + i
    else:
        sum = sum - i
print(sum)

## 用户登陆（三次机会重试）

i = 0
local_name = 'admin'
local_pass = 'pass'
while True:
    name = input("请输入用户名:")
    passwd = input("请输入密码：")

    if name == local_name and passwd == local_pass :
        print('登陆成功')
        break
    else:
        print('用户名密码错误')
        i = i +1
        if i == 3:
            break