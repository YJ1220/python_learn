#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 1、元素分类:将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
List = [11,22,33,44,55,66,77,88,99,90]
value1=[]
value2=[]
for i in List:
    if i >= 66:
        value1.append(i)
    else:
        value2.append(i)
Dict = {'key1':repr(value1),'key2':repr(value2)}
print(Dict)
# 2、查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
li = ["alec", " Aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1':"alex", 'k2':' aric', "k3":"Alex", "k4":"Tony"}

Li=list(map(lambda x:x.strip(),li))
Tu=tuple(map(lambda x:x.strip(),tu))

for key,value in dic.items():
    dic[key]=value.strip()

def evalution(value):
    if value[0] == 'a' or value[0] == 'A' and value[len(value) - 1]  == 'c':
        print(value)

for i in Li:
    evalution(i)
for i in Tu:
    evalution(i)

for i in dic.values():
    evalution(i)

# 3、输出商品列表，用户输入序号，显示用户选中的商品
li = ["手机", "电脑", '鼠标垫', '游艇']

for i,v in enumerate(li,1):
    print(i,v)

# 4、购物车
'''
功能要求：
要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
# 初始化输入资产
while True:
    try:
        property_init = int(input('请输入初始总资产：'))
    except Exception as e:
        print('输入值错误，请重新输入')
        continue
    else:
        print('你的总资产为:{}'.format(property_init))
        break


# 显示商品列表
print('商品列表为：')
for i,v in enumerate(goods,1):
    print(i,v['name'],v['price'])
# 购买商品

shop_car=[]
shop_value=0

def shopping():
    for i in shop_car:
        print('你的购物列表为:%s' % i)
    print('消费总额为:%d' % shop_value)
    print('剩余金额为：%d' % property_init)
while True:
    num_in = input('请输入产品的序列号,如果结束购物请输入q：')
    if num_in == 'q':
        shopping()
        break
    try:
        num=int(num_in)
    except Exception as e:
        print('请输入正确的数字')
        continue
    if num > 4:
        print('输入的产品最大序列号不能超过4')
        continue

    num_key = goods[num-1]['name']
    num_value = goods[num -1]['price']

    print('你选择的商品为"%s"；价格为%d' % (num_key,num_value))
    if property_init > num_value :
        shop_car.append(num_key)
        shop_value=shop_value+num_value
        property_init = property_init - num_value

    else:
        print('你的钱不够')
        shopping()
        break

# 5、用户交互，显示省市县三级联动的选择
    pass






