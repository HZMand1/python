""" 欢迎关注 "码农架构" 微信公众号，热爱开源，拥抱开源。一个IT民工的技术之路经验分享。
    - 问题咨询 / 建议
    1.关注微信公众号 "码农架构" 后私信
    2.可发送邮件: li.shangzhi@aliyun.com
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    for letter in 'Python':  # 第一个实例
        print('当前字母 :', letter)

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # 第二个实例
        print('当前水果 :', fruit)

    fruits = ['banana', 'apple', 'mango']
    # 开始,结束,步长
    for index in range(0, 3, 2):
        print(index)
        print(u'当前水果 :', fruits[index])

    list = [1, 2, 3, 4, 5, 6, 7]
    # range是一个生成器,在操作大量数据的时候不会上来开辟一块很大的内纯空间,形内较好
    for i in range(0, 7, 2):
        print(list[i:i + 2])

    # i 为索引,v为值
    for i, v in enumerate(list):
        print(i, v)

    d2 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
    for k, v in d2.items():
        print(k, v)
