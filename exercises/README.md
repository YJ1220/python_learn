# python练习题
## 第一天
1、使用while循环输入 1 2 3 4 5 6     8 9 10

2、求1-100的所有数的和

3、输出 1-100 内的所有奇数

4、输出 1-100 内的所有偶数

5、求1-2+3-4+5 ... 99的所有数的和

6、用户登陆（三次机会重试）

## 第二天
一、元素分类

有如下值集合 [11,22,33,44,55,66,77,88,99,90...\],
将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

二、查找

查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
    <br>li = \["alec", " aric", "Alex", "Tony", "rain"]
    <br>tu = ("alec", " aric", "Alex", "Tony", "rain")
    <br>dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}

三、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = \["手机", "电脑", '鼠标垫', '游艇']

四、购物车

功能要求：

>要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车

goods = \[
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

五、用户交互，显示省市县三级联动的选择

dic = {
    "河北": {
        "石家庄": \["鹿泉", "藁城", "元氏"],
        "邯郸": \["永年", "涉县", "磁县"],
    }
    "河南": {
        ...
    }
    "山西": {
        ...
    }

}
# 第三天

1、简述普通参数、指定参数、默认参数、动态参数的区别

2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。

5、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

6、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

7、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

dic = {"k1": "v1v1", "k2": \[11,22,33,44]}

PS:字典中的value只能是字符串或列表

8、写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者


　　